from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import os

# Import isolated computational scripts safely
import qna
import explanation_module
import quiz_module
import summary_module
import learning_path

app = FastAPI(title="EduGenie Learning Assistant")

# Bind directories to the framework runtime
os.makedirs("static", exist_ok=True)
os.makedirs("templates", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Explicit Pydantic data schemas for clean inbound form request validation
class QnARequest(BaseModel):
    context: str
    question: str

class ExplanationRequest(BaseModel):
    concept: str
    depth: str

class QuizRequest(BaseModel):
    context: str
    num_questions: int

class SummaryRequest(BaseModel):
    text: str
    format_style: str

class PathRequest(BaseModel):
    goal: str
    timeframe: str

@app.get("/", response_class=HTMLResponse)
async def serve_workspace(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/api/qna")
async def handle_qna(data: QnARequest):
    result = qna.answer_question(data.context, data.question)
    return {"output": result}

@app.post("/api/explain")
async def handle_explain(data: ExplanationRequest):
    result = explanation_module.explain_concept(data.concept, data.depth)
    return {"output": result}

@app.post("/api/quiz")
async def handle_quiz(data: QuizRequest):
    result = quiz_module.generate_quiz(data.context, data.num_questions)
    return {"output": result}

@app.post("/api/summary")
async def handle_summary(data: SummaryRequest):
    result = summary_module.generate_summary(data.text, data.format_style)
    return {"output": result}

@app.post("/api/learning-path")
async def handle_path(data: PathRequest):
    result = learning_path.design_path(data.goal, data.timeframe)
    return {"output": result}
