import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

print("GEMINI KEY FOUND:", API_KEY is not None)

client = genai.Client(api_key=API_KEY)

async def analyze_resume(resume_text: str):
    return {
        "ats_score": 80,
        "skills": ["Python", "SQL", "FastAPI"],
        "strengths": [
            "Good technical background",
            "Clear resume structure"
        ],
        "weaknesses": [
            "Need more project experience"
        ],
        "recommendations": [
            "Add quantified achievements",
            "Add internship experience",
            "Improve ATS keywords"
        ]
    }