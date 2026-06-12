async def generate_roadmap(
    target_role,
    target_company,
    weekly_hours,
    current_skills,
):

    return {
        "total_weeks": 8,
        "weeks": [
            {
                "week": 1,
                "theme": "SQL Fundamentals",
                "topics": ["SELECT", "JOINS", "GROUP BY"],
                "resources": ["SQLBolt"],
                "project": "Sales Analysis",
                "interview_prep": "SQL Questions"
            },
            {
                "week": 2,
                "theme": "Python",
                "topics": ["Pandas", "NumPy"],
                "resources": ["Kaggle"],
                "project": "Data Cleaning",
                "interview_prep": "Python Basics"
            }
        ]
    }