from os import getenv
from random import randint

from dotenv import load_dotenv
from flask import Flask, redirect

from constants import *

load_dotenv()

PORT = getenv('PORT')
DEBUG = getenv('DEBUG') == "True"

app = Flask(__name__)

random_number = randint(1, 10)


@app.get('/')
def home() -> str:
    random_number = randint(1, 10)
    return MENU_TEMPLATE.format(options=GUESSING_OPTION)


@app.get('/guess/<int:number>')
def guess(number: int) -> str:
    if number == random_number:
        return RESULTS_SCREEN.format(message=RIGHT_GUESS_MESSAGE)
    elif number > random_number:
        return redirect("/higher")
    else:
        return redirect("/lower")


@app.get('/higher')
def higher() -> str:
    return HIGHER_GUESS_MESSAGE.format(message=HIGHER_GUESS_MESSAGE)


@app.get('/lower')
def lower() -> str:
    return LOWER_GUESS_MESSAGE.format(message=LOWER_GUESS_MESSAGE)


if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)
