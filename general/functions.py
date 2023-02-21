import base64
import random
import string
from random import randint

from django.core.files.base import ContentFile


"""
To get random password according to the length of n
"""
def random_password(n:int):
    password = []

    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    random.shuffle(characters)

    for i in range(n):
        password.append(random.choice(characters))
    random.shuffle(password)

    return "".join(password)


"""
To get unique id's according to the length of n
"""
def generate_unique_id(n:int):
    unique_id = []
    characters = list(string.ascii_letters + string.digits)
    random.shuffle(characters)

    for i in range(n):
        unique_id.append(random.choice(characters))
    random.shuffle(unique_id)

    return "".join(unique_id)


def randomnumber(n:int):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def convert_base64_image_to_image(base64_image:string,name:string):
    """
         converting base64 image into normal image type
    """
    format, imgstr = base64_image.split(';base64,')
    ext = format.split('/')[-1]
    final_image = ContentFile(base64.b64decode(imgstr), name=f'{name}.{ext}')

    return final_image