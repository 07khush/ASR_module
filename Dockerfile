FROM python:3.10-slim

WORKDIR /app

# system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    ffmpeg \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# python tooling
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# IMPORTANT FIX (torch + whisper compatibility)
RUN pip install --no-cache-dir "numpy<2"

COPY requirements.txt .

# install torch CPU
RUN pip install --no-cache-dir torch==2.2.2 \
    --index-url https://download.pytorch.org/whl/cpu

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy app
COPY . .

# IMPORTANT: allow imports
ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["uvicorn", "whisper_app.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
