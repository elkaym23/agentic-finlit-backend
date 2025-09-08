from langgraph.graph import StateGraph, END
from .schemas import AgentState
from .nodes import node_rag, node_quiz, node_grade, node_coach_or_celebrate

def build_graph():
    g = StateGraph(AgentState)
    g.add_node("rag", node_rag)
    g.add_node("quiz", node_quiz)
    g.add_node("grade", node_grade)
    g.add_node("coach_or_celebrate", node_coach_or_celebrate)

    g.set_entry_point("rag")
    g.add_edge("rag", "quiz")
    g.add_edge("quiz", "grade")
    g.add_edge("grade", "coach_or_celebrate")
    g.add_edge("coach_or_celebrate", END)
    return g.compile()
