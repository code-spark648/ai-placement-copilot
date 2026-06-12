import json
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


async def analyze_job_match(
    resume_text: str,
    job_description: str,
) -> dict:

    prompt = f"""
You are an expert ATS and recruiter.

Compare the resume with the job description.

Return ONLY valid JSON.

{{
  "match_score": 0,
  "missing_keywords": [],
  "missing_skills": [],
  "improvements": []
}}

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    text = response.text.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")

    return json.loads(text)


async def analyze_skill_gap(
    target_role: str,
    current_skills: list,
) -> dict:

    prompt = f"""
You are an expert career coach.

Target Role:
{target_role}

Current Skills:
{", ".join(current_skills)}

Return ONLY valid JSON.

{{
  "target_role": "{target_role}",
  "required_skills": [],
  "present_skills": [],
  "missing_skills": [],
  "skill_score": 0,
  "learning_priorities": [
    {{
      "skill": "",
      "priority": "",
      "reason": "",
      "resource": ""
    }}
  ]
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