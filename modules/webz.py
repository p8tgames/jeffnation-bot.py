#WEBZZZZZZZZ
import requests


def getdoggo():
    dogGif = requests.get('https://api.thedogapi.com/v1/images/search?format=src&mime_types=image/gif')
    if dogGif.status_code == 200:
        dogGif = dogGif.url
        return dogGif

def getkat():
    catGif = requests.get('http://thecatapi.com/api/images/get?format=src&type=gif')
    if catGif.status_code == 200:
        catGif = catGif.url
        return catGif
