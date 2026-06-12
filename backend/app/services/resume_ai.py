import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

print("GEMINI KEY FOUND:", API_KEY is not None)

client = genai.Client(api_key=API_KEY)

async def analyze_resume(resume_text: str):

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents="Say OK"
        )

        print("GEMINI RESPONSE:", response.text)

        return {
            "ats_score": 80,
            "skills": ["Python"],
            "strengths": ["Gemini connected"],
            "weaknesses": [],
            "recommendations": []
        }

    except Exception as e:
        print("GEMINI ERROR:", str(e))
        raise