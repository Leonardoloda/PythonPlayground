from datetime import datetime
from random import randint

from flask import Flask, render_template
from requests import get

app = Flask(__name__)

today = datetime.now()


@app.get("/")
def template():
    # jinga comes by default with flask, it allows you to inject python code
    # if you wanna use imports, you can send custom apraemters
    return render_template(
        "template.html", number=randint(0, 9), current_year=today.year
    )


# You can also receive arguments send by the url_for in an anchor tag
@app.get("/blog/<user>")
def blog(user: str) -> str:
    print(user)
    posts_response = get("https://api.npoint.io/c790b4d5cab58020d391")

    posts = posts_response.json()

    # you can also execute python control structures to render some content
    return render_template("blog.html", posts=posts)


app.run(debug=True, port=8080)
