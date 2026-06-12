async def generate_interview_questions(company: str, role: str):

    return {
        "company": company,
        "role": role,
        "technical_questions": [
            f"Explain a project related to {role}",
            "What is SQL?",
            "What is normalization?",
            "Explain REST APIs",
            "What are joins?"
        ],
        "behavioral_questions": [
            "Tell me about yourself",
            "Describe a challenge you faced",
            "How do you work in teams?"
        ],
        "hr_questions": [
            "Why should we hire you?",
            "Why this company?"
        ]
    }


async def evaluate_interview_answer(
    question: str,
    answer: str,
    company: str | None,
    role: str | None,
):

    return {
        "technical_score": 8,
        "communication_score": 7,
        "confidence_score": 8,
        "feedback": [
            "Good structure",
            "Add more technical depth",
            "Use real examples"
        ]
    }