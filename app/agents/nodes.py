from .schemas import AgentState
from ..db import search_chunks, record_submission
from ..embeddings import embed_query
from ..hf_client import chat

def node_rag(state: AgentState) -> AgentState:
    qvec = embed_query("Key points of this lesson for a Jamaican primary student.")
    hits = search_chunks(state.lesson_id, state.level_slug, qvec, k=6)
    state.context_chunks = [h["content"] for h in hits]
    # Summarize context for the student
    sys = {"role":"system","content":"You are a Jamaican primary school tutor. Keep it simple and friendly."}
    usr = {"role":"user","content": "Summarize these notes in 5 short bullet points:\n" + "\n\n".join(state.context_chunks)}
    state.context_summary = chat([sys, usr], max_new_tokens=180)
    return state

def node_quiz(state: AgentState) -> AgentState:
    sys = {"role":"system","content":"You are a Jamaican primary school teacher. Make kid-friendly multiple-choice questions (A-D) from the provided notes."}
    usr = {"role":"user","content": "Create 5 MCQs. JSON only: {\"items\":[{\"question\":\"...\",\"options\":[\"A\",\"B\",\"C\",\"D\"],\"answer_key\":\"A\"}...]}\nNotes:\n" + "\n\n".join(state.context_chunks)}
    raw = chat([sys, usr], max_new_tokens=350)
    import json
    data = {}
    try: data = json.loads(raw)
    except: data = {"items":[]}
    items = data.get("items", [])[:7]  # 4–7 in your spec
    # Normalize
    fixed = []
    for it in items:
        q = it.get("question","").strip()
        opts = it.get("options", [])[:4]
        while len(opts)<4: opts.append("Option")
        key = str(it.get("answer_key","A")).strip()[:1].upper()
        if key not in "ABCD": key="A"
        if q: fixed.append({"question":q, "options":opts, "answer_key":key, "points":1})
    state.quiz_items = fixed
    return state

def node_grade(state: AgentState) -> AgentState:
    # simple grading
    answers = state.student_answers
    score, total, details = 0, len(state.quiz_items), []
    for i,(it,ans) in enumerate(zip(state.quiz_items, answers)):
        correct = (ans.upper()==it["answer_key"])
        if correct: score += 1
        details.append({"qno":i+1,"user":ans,"key":it["answer_key"],"correct":correct})
    state.score, state.total = score, total
    # record
    if state.assignment_id is None:
        state.assignment_id = 0  # if not assigned formally
    record_submission(state.student_id, quiz_id=0, assignment_id=state.assignment_id,
                      score=score, total=total, details={"items":details})
    return state

def node_coach_or_celebrate(state: AgentState) -> AgentState:
    if state.score == state.total and state.total is not None and state.total>0:
        state.route = "celebrate"
        return state
    # Coach for wrong answers
    wrong = []
    for it,ans in zip(state.quiz_items, state.student_answers):
        if ans.upper()!=it["answer_key"]:
            wrong.append({"q":it["question"],"your":ans,"key":it["answer_key"]})
    sys = {"role":"system","content":"You are a kind tutor. Explain simply where the student went wrong."}
    usr = {"role":"user","content": "Here are the mistakes:\n" + "\n".join([f"Q: {w['q']}\nYour answer: {w['your']}\nCorrect: {w['key']}" for w in wrong]) +
           "\nGive short, friendly explanations for each."}
    state.feedback = chat([sys,usr], max_new_tokens=220)
    state.route = "coach"
    return state
