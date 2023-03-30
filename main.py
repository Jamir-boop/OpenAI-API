import os
import datetime
import openai

openai.organization = "org-zdnx461fIpUGijBFMF2mLK4v"
openai.api_key = os.getenv("OPENAI_API_KEY")


def log_completion(response):
    response = ' '.join(str(response).strip().split('\n'))
    response = response.replace(" ", "")
    log_str = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {response}\n"

    with open("response.log", "a") as f:
        f.write(log_str)


def completionTest(request):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": request}
        ],
        temperature=0
    )
    log_completion(completion)
    return completion


# completion = completionTest("Hello!")
# print(completion.choices[0].message)
