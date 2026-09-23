from gemini_client import generate


def explain_topic(topic: str) -> str:
    prompt = f"""
You are EduGenie, an educational tutor.
Explain the following topic for a beginner.

Topic:
{topic}

Return:
1. Simple definition
2. Main idea
3. Easy example
4. Key points to remember

Use clear headings and simple English.
"""
    return generate(prompt)
