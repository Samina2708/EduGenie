# Project Design

## Architecture
Browser UI (HTML/CSS/JavaScript) → FastAPI routes → task modules → Gemini client/API.

## Main components
- `main.py`: web app, page route, API endpoints, and error handling.
- `schemas.py` and `utils.py`: request shape and shared helpers.
- `qna.py`, `explanation_module.py`, `quiz_module.py`, `summary_module.py`, `learning_path.py`: learning tasks.
- `templates/index.html` and `static/`: user interface.

## API routes present in source
`GET /`, `GET /health`, `POST /qa`, `POST /explain`, `POST /quiz`, `POST /summarize`, and `POST /learn/recommendations`.
