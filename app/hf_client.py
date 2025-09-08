import os
from huggingface_hub import InferenceClient

GEN_MODEL = os.getenv("GEN_MODEL", "mistralai/Mistral-7B-Instruct-v0.2")
HF_TOKEN = os.getenv("HF_TOKEN")
_client = InferenceClient(model=GEN_MODEL, token=HF_TOKEN)

def chat(messages:list[dict], max_new_tokens=256, temperature=0.2) -> str:
    """
    messages: [{"role":"system/user/assistant","content":"..."}]
    returns string
    """
    # Simple conversion to a single prompt; many instruct models handle one turn well.
    system = "\n".join([m["content"] for m in messages if m["role"]=="system"])
    convo  = "\n".join([f"{m['role'].upper()}: {m['content']}" for m in messages if m["role"]!="system"])
    prompt = (system + "\n\n" + convo + "\nASSISTANT:").strip()
    out = _client.text_generation(prompt, max_new_tokens=max_new_tokens, temperature=temperature, stream=False)
    return out
