import re
from typing import Iterable
from .embeddings import embed_texts
from .db import upsert_chunk

def _simple_chunk(text:str, target_len:int=700) -> list[str]:
    # naive splitter by paragraphs into ~700 char chunks
    paras = [p.strip() for p in re.split(r"\n{2,}", text) if p.strip()]
    chunks, buf = [], ""
    for p in paras:
        if len(buf)+len(p) < target_len:
            buf = (buf + "\n\n" + p).strip()
        else:
            if buf: chunks.append(buf)
            buf = p
    if buf: chunks.append(buf)
    return chunks

def ingest_lesson(lesson_id:int, level_slug:str, raw_text:str):
    chunks = _simple_chunk(raw_text)
    embs   = embed_texts(chunks)
    for i, (c,e) in enumerate(zip(chunks, embs), start=1):
        upsert_chunk(lesson_id, level_slug, i, c, e, meta={"source": "preset"})
