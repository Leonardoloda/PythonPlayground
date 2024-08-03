from flask import Flask, render_template
from requests import get

app = Flask(__name__)

posts_response = get("https://api.npoint.io/c790b4d5cab58020d391", timeout=3600)

posts = posts_response.json()


@app.route("/")
def home():
    """Home page for the blog"""
    return render_template("index.html", posts=posts)


@app.get("/<int:post_id>")
def post(post_id: int):
    """Page for each blog"""

    return render_template(
        "post.html", post=[post for post in posts if post["id"] == post_id][0]
    )


if __name__ == "__main__":
    app.run(debug=True)
