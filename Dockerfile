FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Download embedding model at build (faster cold start) - optional
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('intfloat/e5-small-v2')"

COPY app /app/app

EXPOSE 7860
CMD ["uvicorn", "app.main:api", "--host", "0.0.0.0", "--port", "7860"]
