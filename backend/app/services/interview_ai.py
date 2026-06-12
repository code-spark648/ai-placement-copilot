import json
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


async def generate_interview_questions(
    company: str,
    role: str,
) -> dict:

    prompt = f"""
You are a senior interviewer.

Generate interview questions.

Company:
{company}

Role:
{role}

Return ONLY valid JSON.

{{
  "company": "{company}",
  "role": "{role}",
  "technical_questions": [],
  "behavioral_questions": [],
  "hr_questions": []
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    text = response.text.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")

    return json.loads(text)


async def evaluate_interview_answer(
    question: str,
    answer: str,
    company: str | None,
    role: str | None,
) -> dict:

    prompt = f"""
Evaluate this interview answer.

Question:
{question}

Answer:
{answer}

Return ONLY valid JSON.

{{
  "technical_score": 0,
  "communication_score": 0,
  "confidence_score": 0,
  "feedback": []
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    text = response.text.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")

    return json.loads(text)