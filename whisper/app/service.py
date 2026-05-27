import os
import tempfile
from fastapi import UploadFile
from .whisper_model import model


async def transcribe_audio(file: UploadFile) -> dict:
    """
    Save the uploaded file to a temp location, run Whisper medium transcription,
    then clean up. Returns text, language, and segments.
    """
    suffix = os.path.splitext(file.filename)[-1] or ".wav"

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        contents = await file.read()
        tmp.write(contents)
        tmp_path = tmp.name

    try:
        result = model.transcribe(tmp_path)
        return {
            "text": result["text"].strip(),
            "language": result["language"],
            "segments": [
                {
                    "id": seg["id"],
                    "start": round(seg["start"], 2),
                    "end": round(seg["end"], 2),
                    "text": seg["text"].strip(),
                }
                for seg in result.get("segments", [])
            ],
        }
    finally:
        os.remove(tmp_path)
