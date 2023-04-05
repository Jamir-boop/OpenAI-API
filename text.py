import os
import openai
from utils import log_completion

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
    log_completion(completion)
    return completion


completion = completion("Please make a minuta from this transcription ")
# print(completion.choices[0].message)
# procesos de facturacion, cuentas a pagar, area de finanzas, RRHH
