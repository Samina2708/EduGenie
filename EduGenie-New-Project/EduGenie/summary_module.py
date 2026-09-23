from gemini_client import generate


def summarize_text(text: str) -> str:
    prompt = f"""
Summarize the following educational text for a student.

Text:
{text}

Requirements:
- Keep the central meaning.
- Remove repetition.
- Use simple English.
- Prefer short bullet points.
- Do not add information that is not supported by the text.
"""
    return generate(prompt)
