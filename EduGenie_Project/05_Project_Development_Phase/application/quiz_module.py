from gemini_client import generate
from utils import parse_json_response


def generate_quiz(text: str):
    prompt = f"""
Create exactly 3 multiple-choice questions from the educational content below.

Content:
{text}

Return ONLY valid JSON with this exact structure:
{{
  "questions": [
    {{
      "question": "Question text",
      "options": ["A", "B", "C", "D"],
      "answer": "A"
    }}
  ]
}}

Rules:
- Exactly 3 questions.
- Exactly 4 options per question.
- "answer" must exactly match one option.
- Questions must be answerable from the supplied content.
- No Markdown and no extra text.
"""
    data = parse_json_response(generate(prompt))
    questions = data.get("questions", []) if isinstance(data, dict) else data

    if len(questions) != 3:
        raise ValueError("Gemini did not return exactly 3 questions.")

    for q in questions:
        if not all(k in q for k in ("question", "options", "answer")):
            raise ValueError("Quiz response has an invalid question.")
        if len(q["options"]) != 4:
            raise ValueError("Each quiz question must have 4 options.")
        if q["answer"] not in q["options"]:
            raise ValueError("Quiz answer must match an option.")

    return {"questions": questions}
