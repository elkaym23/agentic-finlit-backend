from fastapi import FastAPI

api = FastAPI(title="Agentic FinLit Backend (Starter)")

@api.get("/")
def root():
    return {"ok": True, "service": "agentic-finlit-backend"}
