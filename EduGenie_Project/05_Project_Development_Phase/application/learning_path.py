from gemini_client import generate


def get_learning_recommendations(topic: str) -> str:
    prompt = f"""
Create a personalized learning path for the topic below.

Topic:
{topic}

Structure it as:
- Goal
- Beginner stage
- Intermediate stage
- Advanced stage
- Suggested timeline
- Practice activities
- Useful resource types (videos, articles, books, documentation)

Keep the plan realistic and clear. Do not invent specific URLs.
"""
    return generate(prompt)
