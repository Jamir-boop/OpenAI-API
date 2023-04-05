import os
import openai
from utils import log_completion, local_logger


def transcript(audio_file):
    openai.organization = os.getenv("PUBLIC_ORG")
    openai.api_key = os.getenv("OPENAI_API_KEY")
    audio_file = open("audio.m4a", "rb")
    transcript = openai.Audio.transcribe(
        model="whisper-1",
        file=audio_file,
        language="es",
        temperature="0.2")
    log_completion(transcript, 0)
    local_logger(transcript)


transcript("audio.m4a")
