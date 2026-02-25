# Text-to-Speech (TTS) 

A FastAPI-based Text-to-Speech (TTS)  that converts user input text into natural speech audio using Coqui TTS.

---

##  Features

-  Convert text into natural speech
-  FastAPI backend API
-  Audio streaming response
-  Simple HTML frontend
-  REST API for integration with other services


## Project Structure

text/
│
├── main.py              # FastAPI backend
├── tts_module.py        # TTS processing logic
├── index.html           # Frontend UI
├── requirements.txt     # Dependencies
└── README.md


---

## Technologies Used

- **FastAPI** – Backend API
- **Coqui TTS** – Text-to-Speech model
- **Uvicorn** – ASGI server
- **Pydub** – Audio processing
- **HTML/CSS/JavaScript** – Frontend UI

---

## How It Works

1. User enters text in the frontend.
2. Frontend sends a POST request to `/generate-audio/`.
3. FastAPI calls the TTS model.
4. Audio file is generated.
5. Audio is streamed back to the browser.
6. User listens directly in the webpage.


## Install dependencies
pip install -r requirements.txt


## Run the server
uvicorn main:app --reload

## Open in browser
http://127.0.0.1:8000


