import whisper

# Load once at startup — critical for performance and memory optimization
# Using "medium" model as required
model = whisper.load_model("medium")
