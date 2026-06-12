from fastapi import APIRouter, HTTPException, status
from app.schemas.misc import (
    InterviewQuestionsRequest,
    InterviewQuestionsResponse,
    InterviewEvaluateRequest,
    InterviewEvaluateResponse,
)
from app.services.interview_ai import (
    generate_interview_questions,
    evaluate_interview_answer,
)

router = APIRouter()

SUPPORTED_COMPANIES = [
    "Google",
    "Amazon",
    "Microsoft",
    "Meta",
    "Apple",
    "JPMorgan",
    "Goldman Sachs",
    "Netflix",
    "Uber",
    "Airbnb",
]


@router.post(
    "/questions",
    response_model=InterviewQuestionsResponse,
)
async def get_interview_questions(
    request: InterviewQuestionsRequest,
):
    try:
        result = await generate_interview_questions(
            company=request.company,
            role=request.role,
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Question generation failed: {str(e)}",
        )

    return InterviewQuestionsResponse(**result)


@router.post(
    "/evaluate",
    response_model=InterviewEvaluateResponse,
)
async def evaluate_answer(
    request: InterviewEvaluateRequest,
):
    if not request.question.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Question cannot be empty",
        )

    if not request.answer.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Answer cannot be empty",
        )

    try:
        result = await evaluate_interview_answer(
            question=request.question,
            answer=request.answer,
            company=request.company,
            role=request.role,
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Answer evaluation failed: {str(e)}",
        )

    return InterviewEvaluateResponse(**result)


@router.get("/sessions")
async def get_interview_sessions():
    return []


@router.get("/companies")
async def get_supported_companies():
    return {
        "companies": SUPPORTED_COMPANIES
    }
