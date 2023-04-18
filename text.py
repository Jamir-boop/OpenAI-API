import os
import openai
from utils import response_log

openai.organization = os.getenv("PUBLIC_ORG")
openai.api_key = os.getenv("OPENAI_API_KEY")


def completion(request):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": request}
        ],
        temperature=0
    )
    response_log(completion)
    return completion

with open("request.temp", "r", encoding="utf-8", errors="replace") as file:
    request = file.read()
    completion = completion(request)
    
# print(completion.choices[0].message)
