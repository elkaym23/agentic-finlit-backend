import os
import json
import numpy as np
import pymysql
from contextlib import contextmanager

TIDB_HOST = os.getenv("TIDB_HOST")
TIDB_PORT = int(os.getenv("TIDB_PORT", "4000"))
TIDB_USER = os.getenv("TIDB_USER")
TIDB_PASSWORD = os.getenv("TIDB_PASSWORD")
TIDB_DB = os.getenv("TIDB_DB", "agenticfinance")

@contextmanager
def get_conn():
    conn = pymysql.connect(
        host=TIDB_HOST, port=TIDB_PORT, user=TIDB_USER, password=TIDB_PASSWORD,
        db=TIDB_DB, ssl={"ssl": {}}  # HF -> TiDB usually needs SSL; adjust certs if needed
    )
    try:
        yield conn
    finally:
        conn.close()

def upsert_chunk(lesson_id:int, level_slug:str, position:int, content:str, embedding:np.ndarray, meta:dict=None):
    # Ensure float32 and correct dim 384
    emb = embedding.astype(np.float32).tobytes()
    meta_json = json.dumps(meta or {})
    sql = """
    INSERT INTO lesson_chunks (lesson_id, level_slug, position, content, embedding, meta)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE content=VALUES(content), embedding=VALUES(embedding), meta=VALUES(meta)
    """
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (lesson_id, level_slug, position, content, emb, meta_json))
        conn.commit()

def search_chunks(lesson_id:int, level_slug:str, query_vec:np.ndarray, k:int=6):
    emb = query_vec.astype(np.float32).tobytes()
    sql = """
    SELECT chunk_id, position, content,
           L2_DISTANCE(embedding, %s) AS score
    FROM lesson_chunks
    WHERE lesson_id = %s AND level_slug = %s
    ORDER BY score ASC
    LIMIT %s
    """
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (emb, lesson_id, level_slug, k))
            rows = cur.fetchall()
    return [{"chunk_id":r[0], "position":r[1], "content":r[2], "score":float(r[3])} for r in rows]

def record_submission(student_id:int, quiz_id:int, assignment_id:int, score:int, total:int, details:dict):
    sql = """
    INSERT INTO submissions (assignment_id, quiz_id, student_id, score, total, details)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE score=VALUES(score), total=VALUES(total), details=VALUES(details)
    """
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (assignment_id, quiz_id, student_id, score, total, json.dumps(details)))
        conn.commit()
