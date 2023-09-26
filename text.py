import os
import openai
from dotenv import load_dotenv
from utils import response_log, temp_log

load_dotenv()
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
    temp_log(completion)
    return completion

# with open("request.temp", "r", encoding="utf-8", errors="replace") as file:
#     request = file.read()
#     completion = completion(request)

# completion = completion("Hola mundo")
# print(completion.choices[0].message)
