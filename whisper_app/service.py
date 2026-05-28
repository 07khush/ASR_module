import tempfile
import shutil
from whisper_app.transcribe import transcribe

async def transcribe_audio(file):
    # save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name

    # call whisper
    text = transcribe(tmp_path)

    return {
        "filename": file.filename,
        "text": text
    }
