from flask import Flask, render_template
from requests import get

app = Flask(__name__)

posts_response = get("https://api.npoint.io/674f5423f73deab1e9a7", timeout=3600)

posts = posts_response.json()


@app.get("/")
def home():
    """Home page for the blog"""
    return render_template("index.html", posts=posts, bg_image="static/assets/img/home-bg.jpg", title="Home")


@app.get("/<int:post_id>")
def post(post_id: int):
    """Page for each blog"""
    post = [post for post in posts if post["id"] == post_id][0]
    return render_template(
        "post.html", post=post, title=post["title"], bg_image=post["image_url"]
    )


@app.get("/contact")
def contact_page():
    return render_template("contact.html", title="Contact", bg_image="static/assets/img/contact-bg.jpg")


@app.get("/about")
def about_page():
    return render_template("about.html", title="About", bg_image="static/assets/img/about-bg.jpg")


if __name__ == "__main__":
    app.run(debug=True, port=8080)
