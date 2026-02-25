import re
from num2words import num2words
from TTS.api import TTS
from pydub import AudioSegment

# TTS model (Coqui TTS pre-trained model)
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)



def clean_text(text: str) -> str:
    text = re.sub(r'\d+', lambda x: num2words(int(x.group())), text) 
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9.,?!\'\" ]+', '', text) 
    return text.strip()

def text_to_speech(text: str, output_file: str = "output.wav") -> str:
    """
    Convert text to speech and save as WAV
    """
    cleaned_text = clean_text(text)
    
    # Generate TTS audio
    tts.tts_to_file(text=cleaned_text, file_path=output_file)
    
    # Optional: Load and process audio using pydub if needed
    audio = AudioSegment.from_wav(output_file)
    audio.export(output_file, format="wav") 
    
    return output_file