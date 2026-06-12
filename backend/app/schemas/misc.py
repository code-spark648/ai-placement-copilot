from pydantic import BaseModel
from typing import List, Optional, Any
from uuid import UUID
from datetime import datetime


# Job Match
class JobMatchRequest(BaseModel):
    job_description: str
    resume_text: Optional[str] = None
    job_title: Optional[str] = None


class JobMatchResponse(BaseModel):
    id: UUID
    match_score: int
    missing_keywords: List[str]
    missing_skills: List[str]
    improvements: List[str]
    created_at: datetime

    class Config:
        from_attributes = True


# Skills
class SkillGapRequest(BaseModel):
    target_role: str
    current_skills: List[str]


class SkillGapResponse(BaseModel):
    target_role: str
    required_skills: List[str]
    missing_skills: List[str]
    present_skills: List[str]
    skill_score: int
    learning_priorities: List[dict]


# Roadmap
class RoadmapRequest(BaseModel):
    target_role: str
    target_company: Optional[str] = None
    weekly_hours: int = 10
    current_skills: Optional[List[str]] = []


class RoadmapWeek(BaseModel):
    week: int
    theme: str
    topics: List[str]
    resources: List[str]
    project: Optional[str] = None
    interview_prep: Optional[str] = None


class RoadmapResponse(BaseModel):
    id: UUID
    target_role: str
    target_company: Optional[str] = None
    weekly_hours: int
    total_weeks: int
    weeks: List[Any]
    created_at: datetime

    class Config:
        from_attributes = True


# Interview
class InterviewQuestionsRequest(BaseModel):
    company: str
    role: str


class InterviewEvaluateRequest(BaseModel):
    question: str
    answer: str
    company: Optional[str] = None
    role: Optional[str] = None


class InterviewEvaluateResponse(BaseModel):
    technical_score: float
    communication_score: float
    confidence_score: float
    feedback: List[str]


class InterviewQuestionsResponse(BaseModel):
    company: str
    role: str
    technical_questions: List[str]
    behavioral_questions: List[str]
    hr_questions: List[str]


# Dashboard
class DashboardStats(BaseModel):
    ats_score: float
    job_match_score: float
    skill_score: float
    roadmap_progress: float
    interview_score: float
    placement_readiness: float
    resume_count: int
    interview_count: int
    has_roadmap: bool
    recent_activity: List[dict]
