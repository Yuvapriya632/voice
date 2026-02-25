# main.py

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from tts_module import text_to_speech
import os

# Disable Swagger UI (optional but professional)
app = FastAPI(
    title="Voice & TTS API",
    docs_url=None,
    redoc_url=None
)

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextRequest(BaseModel):
    text: str


# Generate Audio API
@app.post("/generate-audio/")
async def generate_audio(request: TextRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text is required")

    # Generate WAV file
    output_file = text_to_speech(request.text, output_file="output.wav")

    # Return audio so HTML can play it
    audio_file = open(output_file, "rb")
    return StreamingResponse(audio_file, media_type="audio/wav")


# Serve Your HTML Page
@app.get("/")
def serve_html():
    return FileResponse("index.html")