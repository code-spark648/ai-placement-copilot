import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()


API_KEY = os.getenv("GEMINI_API_KEY")

print("GEMINI KEY FOUND:", API_KEY is not None)

if API_KEY:
    print("GEMINI KEY PREFIX:", API_KEY[:15])

client = genai.Client(api_key=API_KEY)




async def analyze_resume(resume_text: str):

    prompt = f"""
You are an ATS Resume Analyzer.

Analyze the resume below.

Return ONLY valid JSON.

{{
    "ats_score": 0,
    "skills": [],
    "strengths": [],
    "weaknesses": [],
    "recommendations": []
}}

Resume:

{resume_text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")

    return json.loads(text)