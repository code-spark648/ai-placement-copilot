from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.job_match import JobMatch
from app.schemas.misc import JobMatchRequest, JobMatchResponse
from app.services.job_match_ai import analyze_job_match

router = APIRouter()


@router.post(
    "/analyze",
    status_code=status.HTTP_200_OK,
)
async def analyze_match(
    request: JobMatchRequest,
    db: Session = Depends(get_db),
):
    resume_text = request.resume_text

    if not resume_text:
        resume_text = """
        Python
        SQL
        Machine Learning
        Data Analysis
        Communication
        Teamwork
        """

    try:
        result = await analyze_job_match(
            resume_text,
            request.job_description,
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"AI analysis failed: {str(e)}",
        )

    return {
        "id": None,
        "job_title": request.job_title,
        "job_description": request.job_description,
        "resume_text": resume_text,
        "match_score": result["match_score"],
        "missing_keywords": result["missing_keywords"],
        "missing_skills": result["missing_skills"],
        "improvements": result["improvements"],
        "created_at": None,
    }


@router.get("/latest")
async def get_latest_match():
    return {
        "message": "Temporarily disabled while fixing authentication"
    }
