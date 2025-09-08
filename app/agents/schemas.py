from pydantic import BaseModel
from typing import List, Optional, Dict

class AgentState(BaseModel):
    student_id: int
    lesson_id: int
    level_slug: str
    assignment_id: Optional[int] = None

    # RAG results
    context_chunks: List[str] = []
    context_summary: Optional[str] = None

    # Quiz
    quiz_items: List[Dict] = []      # [{question, options, answer_key}]
    student_answers: List[str] = []  # ["A","C","B",...]

    # Grading
    score: Optional[int] = None
    total: Optional[int] = None
    feedback: Optional[str] = None
    route: Optional[str] = None      # "coach" | "celebrate"
