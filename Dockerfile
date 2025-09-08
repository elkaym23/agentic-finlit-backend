# backend/Dockerfile
FROM python:3.11-slim

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# your code lives in app/, not src
COPY app/ /app/app
COPY README.md /app/README.md

ENV PORT=7860
EXPOSE 7860

# make sure app/main.py defines FastAPI instance "app"
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]
