FROM python:3.10-slim

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip + ensure setuptools is available globally
RUN pip install --upgrade pip setuptools wheel

# 🔥 IMPORTANT FIX: prevent build isolation issues
ENV PIP_NO_BUILD_ISOLATION=1

# Copy requirements first
COPY requirements.txt .

# Install PyTorch CPU
RUN pip install --no-cache-dir \
    torch==2.2.2 \
    --index-url https://download.pytorch.org/whl/cpu

# Install other dependencies (including whisper)
RUN pip install --no-cache-dir \
    -r requirements.txt \
    --extra-index-url https://download.pytorch.org/whl/cpu

# Copy full project
COPY . .

EXPOSE 8000

# IMPORTANT: match your structure
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
