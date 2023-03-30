import os
import openai
from main import log_completion


def imageCreation(request):
    openai.organization = "org-nybR30PBgNsHj4MpSOxYpDoh"
    openai.api_key = os.getenv("PERSONAL_API_KEY")

    image = openai.Image.create(
        prompt=request,
        n=10,
        size="1024x1024"
    )
    log_completion(image)
    return image


def imageEdit(pathImage, pathImageMask, prompt):
    openai.organization = "org-nybR30PBgNsHj4MpSOxYpDoh"
    openai.api_key = os.getenv("PERSONAL_API_KEY")
    response = openai.Image.create_edit(
        image=open(pathImage, "rb"),
        mask=open(pathImageMask, "rb"),
        prompt=prompt,
        n=10,
        size="1024x1024"
    )
    log_completion(response)
    return response


def imageVariation(pathImage):
    openai.organization = "org-nybR30PBgNsHj4MpSOxYpDoh"
    openai.api_key = os.getenv("PERSONAL_API_KEY")
    image = openai.Image.create_variation(
        image=open(pathImage, "rb"),
        n=2,
        size="1024x1024"
    )
    log_completion(image)
    return image


# imageCreation("digital paint cute baby cat with his brothers in a warm mood")
# imageVariation("DALL·E 2023-03-13 09.20.26 - add a suit.png")
imageEdit("DALL·E 2023-03-13 09.20.26 - add a suit.png", "mask.png", "add a watch")