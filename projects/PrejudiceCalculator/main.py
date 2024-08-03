from client import Client
from constants import AGIFY_API, GENDERIZE_API
from flask import Flask, render_template

client = Client()

params = {"name": "Leo"}

client.url = AGIFY_API

age_response = client.fetch_response(params)

client.url = GENDERIZE_API

gender_response = client.fetch_response(params)

age = age_response["age"]
gender = gender_response["gender"]


app = Flask(__name__)


@app.get("/<name>")
def guess(name: str):
    """Accepts a name and returns info about that name"""
    return render_template("Home.html", name=name, age=10, gender="M")


if __name__ == "__main__":
    app.run(debug=True, port=8080)
