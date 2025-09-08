# Use a version most libs actually support
FROM python:3.11-slim

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Basic build deps if wheels aren’t available
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl git \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps first for better layer cache
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy your actual code. You don’t have src/, you have app/
COPY app/ /app/app
COPY README.md /app/README.md

# Hugging Face passes PORT. Use it.
ENV PORT=7860
EXPOSE 7860

# Start your FastAPI app
# Option A: uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]
# If you prefer python main.py, use the line below instead and delete uvicorn above:
# CMD ["python", "-m", "app.main"]
