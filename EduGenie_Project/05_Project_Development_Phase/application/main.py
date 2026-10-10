from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from google.genai.errors import ClientError

from schemas import TaskRequest
from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="EduGenie",
    description="Google Gemini powered learning assistant",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.exception_handler(ClientError)
async def handle_gemini_error(_request: Request, exc: ClientError):
    del _request
    if exc.code == 429:
        return JSONResponse(
            status_code=429,
            content={"detail": "Gemini quota is temporarily exhausted. Please wait and try again, or use a billing-enabled API key."},
        )
    return JSONResponse(
        status_code=502,
        content={"detail": "The AI service is temporarily unavailable. Check your API key and connection."},
    )


@app.exception_handler(Exception)
async def handle_unexpected_error(_request: Request, _exc: Exception):
    del _request, _exc
    return JSONResponse(
        status_code=502,
        content={"detail": "The AI service is temporarily unavailable. Check your connection and try again."},
    )


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(BASE_DIR / "static" / "favicon.svg", media_type="image/svg+xml")


@app.get("/health")
async def health():
    return {"status": "ok", "service": "EduGenie"}


@app.post("/qa")
async def qa(payload: TaskRequest):
    return {"result": answer_question(payload.text)}


@app.post("/explain")
async def explain(payload: TaskRequest):
    return {"result": explain_topic(payload.text)}


@app.post("/quiz")
async def quiz(payload: TaskRequest):
    return {"result": generate_quiz(payload.text)}


@app.post("/summarize")
async def summarize(payload: TaskRequest):
    return {"result": summarize_text(payload.text)}


@app.post("/learn/recommendations")
async def recommendations(payload: TaskRequest):
    return {"result": get_learning_recommendations(payload.text)}
