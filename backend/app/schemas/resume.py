from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID
from datetime import datetime


class ResumeAnalysis(BaseModel):
    ats_score: int
    skills: List[str]
    strengths: List[str]
    weaknesses: List[str]
    recommendations: List[str]


class ResumeResponse(BaseModel):
    id: UUID
    filename: str
    ats_score: Optional[int] = None
    skills: Optional[List[str]] = []
    strengths: Optional[List[str]] = []
    weaknesses: Optional[List[str]] = []
    recommendations: Optional[List[str]] = []
    created_at: datetime

    class Config:
        from_attributes = True
