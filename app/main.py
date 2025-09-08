from fastapi import FastAPI
from pydantic import BaseModel
from .agents.schemas import AgentState
from .agents.graph import build_graph
from .ingest import ingest_lesson

api = FastAPI(title="Agentic FinLit Backend")
_graph = build_graph()

class StartRun(BaseModel):
    student_id: int
    lesson_id: int
    level_slug: str

class SubmitQuiz(BaseModel):
    student_id: int
    lesson_id: int
    level_slug: str
    answers: list[str]
    assignment_id: int | None = None

@api.post("/ingest")
def ingest(lesson_id:int, level_slug:str, raw_text:str):
    ingest_lesson(lesson_id, level_slug, raw_text)
    return {"ok": True}

@api.post("/agent/start")
def agent_start(payload: StartRun):
    state = AgentState(**payload.model_dump())
    out = _graph.invoke(state, start_at="rag")
    return {"summary": out.context_summary, "ok": True}

@api.post("/agent/quiz")
def agent_quiz(payload: StartRun):
    state = AgentState(**payload.model_dump())
    out = _graph.invoke(state, start_at="quiz")
    return {"items": out.quiz_items}

@api.post("/agent/grade")
def agent_grade(payload: SubmitQuiz):
    st = AgentState(student_id=payload.student_id, lesson_id=payload.lesson_id,
                    level_slug=payload.level_slug, assignment_id=payload.assignment_id)
    st.student_answers = payload.answers
    out = _graph.invoke(st, start_at="grade")
    return {"score": out.score, "total": out.total}

@api.post("/agent/coach_or_celebrate")
def agent_next(payload: SubmitQuiz):
    st = AgentState(student_id=payload.student_id, lesson_id=payload.lesson_id,
                    level_slug=payload.level_slug, assignment_id=payload.assignment_id)
    st.student_answers = payload.answers
    out = _graph.invoke(st, start_at="coach_or_celebrate")
    data = {"route": out.route}
    if out.route == "coach":
        data["feedback"] = out.feedback
    else:
        data["message"] = "Great job! Want to play Money Match?"
        data["game_slug"] = "money_match"
    return data
