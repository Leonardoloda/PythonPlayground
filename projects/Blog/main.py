from datetime import datetime
from os import getenv

from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditorField, CKEditor
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired, URL

from email_client import EmailClient

load_dotenv()

EMAIL = getenv('EMAIL')
PASSWORD = getenv('PASSWORD')

client = EmailClient(EMAIL, PASSWORD)

app = Flask(__name__)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

app.config['CKEDITOR_PKG_TYPE'] = 'basic'
ckeditor = CKEditor(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.get("/")
def home_page():
    posts = db.session.query(BlogPost).order_by(BlogPost.date).all()

    """Home page for the blog"""
    return render_template("index.html", posts=posts, bg_image="static/assets/img/home-bg.jpg", title="Home")


@app.get("/<int:post_id>")
def post(post_id: int):
    post = db.session.query(BlogPost).get(post_id)

    return render_template(
        "post.html", post=post, title=post.title, bg_image=post.img_url
    )


class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    img_url = StringField('Image', validators=[DataRequired(), URL()])
    submit = SubmitField(label="Submit")

    body = body = CKEditorField('Body')


@app.route("/publish", methods=['GET', 'POST'])
def publish_page():
    publish_form = BlogPostForm()

    print("errors", publish_form.errors)

    if request.method == "POST" and publish_form.validate():
        title = publish_form.title.data
        subtitle = publish_form.subtitle.data
        author = publish_form.author.data
        image = publish_form.img_url.data
        body = publish_form.body.data
        today = datetime.today()

        post = BlogPost(title=title, subtitle=subtitle, author=author, img_url=image, body=body,
                        date=today.strftime("%B %d, %Y"))

        db.session.add(post)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("make-post.html", form=publish_form)


@app.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit_page(post_id: int):
    post = db.session.query(BlogPost).get(post_id)

    edit_form = BlogPostForm(
        title=post.title,
        subtitle=post.subtitle,
        author=post.author,
        img_url=post.img_url,
        body=post.body
    )

    if request.method == "POST" and edit_form.validate():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.author = edit_form.author.data
        post.img_url = edit_form.img_url.data
        post.body = edit_form.body.data

        db.session.commit()

        return redirect(url_for("post", post_id=post.id))

    return render_template("make-post.html", form=edit_form, title="Edit Post")


@app.get("/delete/<int:post_id>")
def delete(post_id: int):
    post = db.session.query(BlogPost).get(post_id)

    db.session.delete(post)
    db.session.commit()

    return redirect(url_for("home_page"))


@app.get("/contact")
def contact_page():
    return render_template("contact.html", title="Contact", bg_image="static/assets/img/contact-bg.jpg")


@app.post("/contact")
def submit_form():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    message = request.form.get("message")

    subject = "A new person has interacted with your blog"
    body = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        
        Message: 
        {message}
    """

    client.send_email(email=EMAIL, subject=subject, body=body)

    return "Contact form submitted"


@app.get("/about")
def about_page():
    return render_template("about.html", title="About", bg_image="static/assets/img/about-bg.jpg")


if __name__ == "__main__":
    app.run(debug=True, port=8080)
