import json
import os
from typing import Optional

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


async def generate_roadmap(
    target_role: str,
    target_company: Optional[str],
    weekly_hours: int,
    current_skills: list,
):

    prompt = f"""
You are a world-class placement mentor and career coach.

Generate a HIGHLY PERSONALIZED 8-week roadmap.

Candidate Details:

Target Role: {target_role}

Target Company: {target_company}

Weekly Hours Available: {weekly_hours}

Current Skills: {', '.join(current_skills)}

IMPORTANT:

- Different roles MUST get different roadmaps.
- Different companies MUST influence preparation.
- Consider current skills and avoid teaching already known topics.
- Include projects directly relevant to the target role.
- Include interview preparation every week.
- Include modern tools used in industry.
- Make the roadmap practical and placement-focused.

Examples:

Data Analyst:
- SQL
- Excel
- Power BI
- Statistics
- Dashboard Projects

Data Scientist:
- Python
- Statistics
- Machine Learning
- Deep Learning
- End-to-End ML Projects

Backend Developer:
- APIs
- FastAPI
- Databases
- Docker
- System Design

Frontend Developer:
- HTML
- CSS
- JavaScript
- React
- TypeScript

Machine Learning Engineer:
- Python
- Deep Learning
- MLOps
- Deployment
- Model Monitoring

DevOps Engineer:
- Linux
- AWS
- Docker
- Kubernetes
- CI/CD

Return ONLY valid JSON.

{{
  "total_weeks": 8,
  "weeks": [
    {{
      "week": 1,
      "theme": "",
      "topics": [],
      "resources": [],
      "project": "",
      "interview_prep": ""
    }}
  ]
}}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
    except Exception:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )

    text = response.text.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    try:
        return json.loads(text)

    except Exception:
        return {
            "total_weeks": 8,
            "weeks": [
                {
                    "week": 1,
                    "theme": "Career Planning",
                    "topics": [
                        "Role Research",
                        "Industry Overview"
                    ],
                    "resources": [
                        "Official Documentation"
                    ],
                    "project": "Starter Project",
                    "interview_prep": "Basic Interview Questions"
                }
            ]
        }