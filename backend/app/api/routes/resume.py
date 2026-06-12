from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, status
from sqlalchemy.orm import Session
import io
import PyPDF2

from app.db.session import get_db
from app.schemas.resume import ResumeResponse
from app.services.resume_ai import analyze_resume

router = APIRouter()


def extract_text_from_pdf(file_bytes: bytes) -> str:
    try:
        reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        return text.strip()

    except Exception as e:
        raise ValueError(f"Failed to extract PDF text: {str(e)}")


@router.post(
    "/upload",
    response_model=ResumeResponse,
    status_code=status.HTTP_201_CREATED,
)
async def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF files are accepted",
        )

    file_bytes = await file.read()

    if len(file_bytes) > 5 * 1024 * 1024:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File size must be under 5MB",
        )

    try:
        raw_text = extract_text_from_pdf(file_bytes)

        if not raw_text or len(raw_text) < 50:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Could not extract meaningful text from PDF.",
            )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )

    try:
        analysis = await analyze_resume(raw_text)

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"AI analysis failed: {str(e)}",
        )

    return {
        "id": "11111111-1111-1111-1111-111111111111",
        "filename": file.filename,
        "ats_score": analysis["ats_score"],
        "skills": analysis["skills"],
        "strengths": analysis["strengths"],
        "weaknesses": analysis["weaknesses"],
        "recommendations": analysis["recommendations"],
        "created_at": "2026-06-12T12:00:00",
    }


@router.get("/latest")
async def get_latest_resume():
    return {
        "message": "Temporary endpoint"
    }


@router.get("/all")
async def get_all_resumes():
    return []