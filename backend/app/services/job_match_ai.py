async def analyze_job_match(
    resume_text: str,
    job_description: str,
):

    return {
        "match_score": 76,
        "missing_keywords": [
            "Power BI",
            "Tableau"
        ],
        "missing_skills": [
            "SQL Optimization"
        ],
        "improvements": [
            "Add analytics projects",
            "Add dashboard experience"
        ]
    }


async def analyze_skill_gap(
    target_role: str,
    current_skills: list,
):

    return {
        "target_role": target_role,
        "required_skills": [
            "Python",
            "SQL",
            "Power BI",
            "Statistics"
        ],
        "present_skills": current_skills,
        "missing_skills": [
            "Power BI",
            "Statistics"
        ],
        "skill_score": 70,
        "learning_priorities": [
            {
                "skill": "Power BI",
                "priority": "High",
                "reason": "Used heavily in industry",
                "resource": "Microsoft Learn"
            }
        ]
    }