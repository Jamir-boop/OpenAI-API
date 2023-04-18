import os
import openai
from utils import response_log


def imageCreation(request):
    openai.organization = os.getenv("PERSONAL_ORG")
    openai.api_key = os.getenv("PERSONAL_API_KEY")

    image = openai.Image.create(
        prompt=request,
        n=10,
        size="1024x1024"
    )
    response_log(image)
    return image


def imageEdit(pathImage, pathImageMask, prompt):
    openai.organization = os.getenv("PERSONAL_ORG")
    openai.api_key = os.getenv("PERSONAL_API_KEY")
    response = openai.Image.create_edit(
        image=open(pathImage, "rb"),
        mask=open(pathImageMask, "rb"),
        prompt=prompt,
        n=2,
        size="1024x1024"
    )
    response_log(response)
    return response


def imageVariation(pathImage):
    openai.organization = os.getenv("PERSONAL_ORG")
    openai.api_key = os.getenv("PERSONAL_API_KEY")
    image = openai.Image.create_variation(
        image=open(pathImage, "rb"),
        n=2,
        size="1024x1024"
    )
    response_log(image)
    return image


# imageCreation("digital paint cute baby cat with his brothers in a warm mood")
# imageVariation("y.png")
# imageEdit("l.png", "mask.png", "add a creepy background and feets")
