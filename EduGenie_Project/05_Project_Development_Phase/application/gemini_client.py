from functools import lru_cache
from google import genai
from config import GEMINI_API_KEY, GEMINI_MODEL, MAX_INPUT_CHARS


@lru_cache(maxsize=1)
def get_client():
    return genai.Client(api_key=GEMINI_API_KEY)


def generate(prompt: str) -> str:
    if not prompt or not prompt.strip():
        raise ValueError("Input cannot be empty.")

    prompt = prompt.strip()
    if len(prompt) > MAX_INPUT_CHARS:
        prompt = prompt[:MAX_INPUT_CHARS]

    response = get_client().models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
    )

    text = getattr(response, "text", None)
    if not text:
        raise RuntimeError("Gemini returned an empty response.")
    return text.strip()
