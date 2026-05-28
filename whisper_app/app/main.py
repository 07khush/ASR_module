from fastapi import FastAPI, UploadFile, File
from whisper_app.service import transcribe_audio

app = FastAPI(title="Whisper API")

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    result = await transcribe_audio(file)
    return result
