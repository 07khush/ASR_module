FROM python:3.10-slim

WORKDIR /app

# System deps (optional but useful for many Python packages)
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip + install setuptools/wheel
RUN python -m pip install --upgrade pip setuptools wheel

# Copy requirements first (better Docker caching)
COPY requirements.txt .

# Install PyTorch CPU
RUN pip install --no-cache-dir \
    torch==2.2.2 \
    --index-url https://download.pytorch.org/whl/cpu

# Install remaining dependencies
RUN pip install --no-cache-dir \
    -r requirements.txt \
    --extra-index-url https://download.pytorch.org/whl/cpu

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Start FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
