# EduGenie — Google Gemini Powered Learning Assistant

EduGenie is a lightweight educational assistant built with FastAPI, HTML/CSS/JavaScript, and the Google Gemini API.

## Features

- Q&A
- Beginner-friendly concept explanation
- 3-question MCQ quiz generation
- Text summarization
- Personalized learning path

## Project structure

```text
EduGenie/
├── main.py
├── config.py
├── gemini_client.py
├── schemas.py
├── utils.py
├── qna.py
├── explanation_module.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── app.js
└── tests/
    └── test_app.py
```

## Requirements

- Python 3.10+
- A Gemini API key
- Internet connection for Gemini requests

## VS Code setup

### Windows

Open the project folder in VS Code, then open **Terminal → New Terminal**:

```powershell
py -3.10 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
copy .env.example .env
```

Open `.env` and replace `your_api_key_here` with your Gemini API key.

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
```

Then edit `.env` and add your Gemini API key.

## Run

```bash
python -m uvicorn main:app --reload
```

Open:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs

Health check:

http://127.0.0.1:8000/health

## Test

With the virtual environment activated:

```bash
pytest -q
```

The included tests verify the application routes and validation without making real Gemini calls.

## Security

Never put your API key in HTML, JavaScript, Git, or source code. The browser calls FastAPI; FastAPI calls Gemini. Keep `.env` private.

For production, use a proper secret manager and apply API-key restrictions.
