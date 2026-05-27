FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip setuptools wheel

COPY requirements.txt .

RUN pip install --no-cache-dir \
    torch==2.2.2 \
    --index-url https://download.pytorch.org/whl/cpu

RUN pip install --no-cache-dir \
    -r requirements.txt \
    --extra-index-url https://download.pytorch.org/whl/cpu

# ✅ IMPORTANT: copy full project
COPY . .

EXPOSE 8000

# FIXED PATH (based on your structure)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
