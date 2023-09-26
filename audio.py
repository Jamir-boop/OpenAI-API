import os
import openai
from dotenv import load_dotenv
from utils import response_log, temp_log

load_dotenv()
openai.organization = os.getenv("PUBLIC_ORG")
openai.api_key = os.getenv("OPENAI_API_KEY")

def transcript(audio_file):
    audio_file = open(audio_file, "rb")
    transcript = openai.Audio.transcribe(
        model="whisper-1",
        file=audio_file,
        language="es",
        temperature="0.2")
    response_log(transcript, remove_spaces=0)
    temp_log(transcript)


transcript("C:/Users/vargas/Downloads/WhatsApp Audio 2023-09-26 at 2.24.34 PM_trimmed.mp3")