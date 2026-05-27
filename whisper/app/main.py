from fastapi import FastAPI
from pydantic import BaseModel
import torch

app = FastAPI(
    title="FastAPI App",
    description="Working FastAPI server with PyTorch",
    version="1.0.0"
)

device = "cuda" if torch.cuda.is_available() else "cpu"


class InputData(BaseModel):
    text: str


@app.get("/")
async def root():
    return {
        "status": "success",
        "message": "FastAPI server is running",
        "torch_version": torch.__version__,
        "device": device
    }


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.post("/predict")
async def predict(data: InputData):
    return {
        "input_text": data.text,
        "text_length": len(data.text),
        "device": device,
        "prediction": "success"
    }
