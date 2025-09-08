import os
import numpy as np
from sentence_transformers import SentenceTransformer

EMBED_MODEL = os.getenv("EMBED_MODEL", "intfloat/e5-small-v2")
_embedder = SentenceTransformer(EMBED_MODEL)

def embed_texts(texts:list[str]) -> list[np.ndarray]:
    # e5 expects "query: ..." and "passage: ..." for some modes; standard encode works fine here
    embs = _embedder.encode(texts, normalize_embeddings=False, convert_to_numpy=True)
    return [np.asarray(e, dtype="float32") for e in embs]

def embed_query(text:str) -> np.ndarray:
    return embed_texts([text])[0]
