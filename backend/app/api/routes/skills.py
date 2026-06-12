from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.misc import SkillGapRequest, SkillGapResponse
from app.services.job_match_ai import analyze_skill_gap

router = APIRouter()

VALID_ROLES = [
    "Software Engineer",
    "Data Analyst",
    "Data Scientist",
    "Product Manager",
    "Frontend Developer",
    "Backend Developer",
    "Full Stack Developer",
    "Machine Learning Engineer",
    "DevOps Engineer",
    "Cloud Engineer",
]


@router.post("/gap-analysis", response_model=SkillGapResponse)
async def skill_gap_analysis(
    request: SkillGapRequest,
    db: Session = Depends(get_db),
):
    if not request.target_role.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Target role cannot be empty",
        )

    try:
        result = await analyze_skill_gap(
            request.target_role,
            request.current_skills,
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Skill gap analysis failed: {str(e)}",
        )

    return SkillGapResponse(**result)


@router.get("/roles")
async def get_valid_roles():
    return {"roles": VALID_ROLES}
