import whisper

model = whisper.load_model("small")

audio_file = "/home/khushi/whisper_model/main/whisper/test.wav"

result = model.transcribe(audio_file)

print(result["text"])
