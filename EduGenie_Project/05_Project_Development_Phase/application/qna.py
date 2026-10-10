from gemini_client import generate


def answer_question(question: str) -> str:
    prompt = f"""
You are EduGenie, a friendly educational assistant.
Answer the student's question accurately and concisely.

Question:
{question}

Rules:
- Use simple English.
- Explain important terms briefly.
- If the question needs steps, use numbered steps.
- Do not invent sources or facts.
"""
    return generate(prompt)
