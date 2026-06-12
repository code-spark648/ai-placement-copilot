from fastapi import APIRouter, HTTPException, status

from app.schemas.misc import RoadmapRequest
from app.services.roadmap_ai import generate_roadmap

router = APIRouter()


@router.post("/generate")
async def create_roadmap(request: RoadmapRequest):

    if request.weekly_hours < 1 or request.weekly_hours > 80:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Weekly hours must be between 1 and 80",
        )

    try:
        result = await generate_roadmap(
            target_role=request.target_role,
            target_company=request.target_company,
            weekly_hours=request.weekly_hours,
            current_skills=request.current_skills or [],
        )

        return result

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )


@router.get("/latest")
async def get_latest_roadmap():
    return {
        "message": "Roadmap history disabled in public mode"
    }


@router.get("/all")
async def get_all_roadmaps():
    return []