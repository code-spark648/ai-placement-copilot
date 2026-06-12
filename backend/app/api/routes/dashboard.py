from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from app.db.session import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.models.resume import Resume
from app.models.job_match import JobMatch
from app.models.roadmap import Roadmap
from app.models.interview import InterviewSession
from app.models.readiness import ReadinessScore
from app.schemas.misc import DashboardStats

router = APIRouter()


def calculate_placement_readiness(
    ats_score: float,
    job_match_score: float,
    skill_score: float,
    roadmap_progress: float,
    interview_score: float,
) -> float:
    """
    Weighted average of all scores to compute overall placement readiness.
    Weights: ATS(20%) + JobMatch(25%) + Skills(25%) + Roadmap(15%) + Interview(15%)
    """
    weighted = (
        ats_score * 0.20
        + job_match_score * 0.25
        + skill_score * 0.25
        + roadmap_progress * 0.15
        + interview_score * 0.15
    )
    return round(min(weighted, 100.0), 1)


@router.get("/stats", response_model=DashboardStats)
async def get_dashboard_stats(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    # --- ATS Score: latest resume ---
    latest_resume = (
        db.query(Resume)
        .filter(Resume.user_id == current_user.id)
        .order_by(Resume.created_at.desc())
        .first()
    )
    ats_score = float(latest_resume.ats_score) if latest_resume and latest_resume.ats_score else 0.0

    # --- Job Match Score: average of last 3 matches ---
    recent_matches = (
        db.query(JobMatch)
        .filter(JobMatch.user_id == current_user.id)
        .order_by(JobMatch.created_at.desc())
        .limit(3)
        .all()
    )
    if recent_matches:
        job_match_score = float(
            sum(m.match_score for m in recent_matches if m.match_score) / len(recent_matches)
        )
    else:
        job_match_score = 0.0

    # --- Skill Score: placeholder (users can set via skill gap analysis) ---
    # We derive from resume skills count as a proxy if no explicit skill analysis
    skill_score = 0.0
    if latest_resume and latest_resume.skills:
        # Rough proxy: more skills → higher score, capped at 85
        skill_count = len(latest_resume.skills)
        skill_score = min(float(skill_count * 5), 85.0)

    # --- Roadmap Progress: based on weeks elapsed vs total weeks ---
    latest_roadmap = (
        db.query(Roadmap)
        .filter(Roadmap.user_id == current_user.id)
        .order_by(Roadmap.created_at.desc())
        .first()
    )
    roadmap_progress = 0.0
    has_roadmap = False
    if latest_roadmap and latest_roadmap.total_weeks:
        has_roadmap = True
        days_elapsed = (datetime.utcnow() - latest_roadmap.created_at.replace(tzinfo=None)).days
        weeks_elapsed = days_elapsed / 7
        roadmap_progress = min(
            float((weeks_elapsed / latest_roadmap.total_weeks) * 100), 100.0
        )

    # --- Interview Score: average across all scores in last 5 sessions ---
    recent_sessions = (
        db.query(InterviewSession)
        .filter(InterviewSession.user_id == current_user.id)
        .order_by(InterviewSession.created_at.desc())
        .limit(5)
        .all()
    )
    interview_score = 0.0
    if recent_sessions:
        avg_scores = []
        for s in recent_sessions:
            scores = [x for x in [s.technical_score, s.communication_score, s.confidence_score] if x is not None]
            if scores:
                avg_scores.append(sum(scores) / len(scores))
        if avg_scores:
            # Sessions are scored 0–10; normalize to 0–100
            interview_score = float((sum(avg_scores) / len(avg_scores)) * 10)

    # --- Placement Readiness ---
    placement_readiness = calculate_placement_readiness(
        ats_score, job_match_score, skill_score, roadmap_progress, interview_score
    )

    # --- Persist readiness snapshot ---
    readiness = ReadinessScore(
        user_id=current_user.id,
        ats_score=ats_score,
        job_match_score=job_match_score,
        skill_score=skill_score,
        roadmap_progress=roadmap_progress,
        interview_score=interview_score,
        placement_readiness=placement_readiness,
    )
    db.add(readiness)
    db.commit()

    # --- Recent Activity ---
    recent_activity = []

    if latest_resume:
        recent_activity.append({
            "type": "resume",
            "label": f"Resume analyzed – ATS score {latest_resume.ats_score}",
            "timestamp": latest_resume.created_at.isoformat(),
        })

    for m in recent_matches[:2]:
        recent_activity.append({
            "type": "job_match",
            "label": f"Job match analyzed – {m.match_score}% match",
            "timestamp": m.created_at.isoformat(),
        })

    if latest_roadmap:
        recent_activity.append({
            "type": "roadmap",
            "label": f"Roadmap generated for {latest_roadmap.target_role}",
            "timestamp": latest_roadmap.created_at.isoformat(),
        })

    for s in recent_sessions[:2]:
        avg = sum(x for x in [s.technical_score, s.communication_score, s.confidence_score] if x) / 3
        recent_activity.append({
            "type": "interview",
            "label": f"Mock interview completed – avg score {avg:.1f}/10",
            "timestamp": s.created_at.isoformat(),
        })

    # Sort by timestamp descending
    recent_activity.sort(key=lambda x: x["timestamp"], reverse=True)

    return DashboardStats(
        ats_score=ats_score,
        job_match_score=job_match_score,
        skill_score=skill_score,
        roadmap_progress=roadmap_progress,
        interview_score=interview_score,
        placement_readiness=placement_readiness,
        resume_count=db.query(Resume).filter(Resume.user_id == current_user.id).count(),
        interview_count=db.query(InterviewSession).filter(InterviewSession.user_id == current_user.id).count(),
        has_roadmap=has_roadmap,
        recent_activity=recent_activity[:6],
    )


@router.get("/readiness-history")
async def get_readiness_history(
    days: int = 30,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    since = datetime.utcnow() - timedelta(days=days)
    scores = (
        db.query(ReadinessScore)
        .filter(
            ReadinessScore.user_id == current_user.id,
            ReadinessScore.created_at >= since,
        )
        .order_by(ReadinessScore.created_at.asc())
        .all()
    )
    return [
        {
            "date": s.created_at.strftime("%Y-%m-%d"),
            "placement_readiness": s.placement_readiness,
            "ats_score": s.ats_score,
            "interview_score": s.interview_score,
        }
        for s in scores
    ]
