ROLE_SKILLS = {
    "data analyst": [
        "SQL",
        "Excel",
        "Power BI",
        "Python",
        "Statistics"
    ],

    "software engineer": [
        "Python",
        "Git",
        "Docker",
        "AWS",
        "System Design"
    ],

    "machine learning engineer": [
        "Python",
        "TensorFlow",
        "PyTorch",
        "Machine Learning",
        "Statistics"
    ]
}


async def analyze_skill_gap(
    target_role: str,
    current_skills: list,
):

    role = target_role.lower()

    required = ROLE_SKILLS.get(
        role,
        ROLE_SKILLS["software engineer"]
    )

    present = [
        skill.strip()
        for skill in current_skills
    ]

    missing = [
        skill
        for skill in required
        if skill not in present
    ]

    score = int(
        (len(present) / len(required)) * 100
    )

    return {
        "target_role": target_role,
        "required_skills": required,
        "present_skills": present,
        "missing_skills": missing,
        "skill_score": min(score, 100),
        "learning_priorities": missing
    }