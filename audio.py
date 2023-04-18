import os
import openai
from utils import response_log, temp_log


def transcript(audio_file):
    openai.organization = os.getenv("PUBLIC_ORG")
    openai.api_key = os.getenv("OPENAI_API_KEY")
    audio_file = open(audio_file, "rb")
    transcript = openai.Audio.transcribe(
        model="whisper-1",
        file=audio_file,
        language="es",
        temperature="0.2")
    response_log(transcript, remove_spaces=0)
    temp_log(transcript)


# transcript("audio.mp3")
