from os import urandom

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy.orm import MappedColumn, Mapped, DeclarativeBase
from wtforms import StringField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, length, NumberRange, URL

app = Flask(__name__)

app.config['SECRET_KEY'] = urandom(32)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"

Bootstrap5(app)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

db.init_app(app)


class Movie(db.Model):
    __tablename__ = 'movies'
    id: Mapped[int] = MappedColumn(db.Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = MappedColumn(db.String, nullable=False)
    year: Mapped[int] = MappedColumn(db.Integer, nullable=False)
    description: Mapped[str] = MappedColumn(db.String, nullable=False)
    rating: Mapped[int] = MappedColumn(db.Integer, nullable=False)
    ranking: Mapped[int] = MappedColumn(db.Integer, nullable=False)
    review: Mapped[str] = MappedColumn(db.Integer, nullable=False)
    img_url: Mapped[str] = MappedColumn(db.String, nullable=False)


class MovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), length(min=1, max=50)])
    year = IntegerField('Year', validators=[DataRequired(), NumberRange(min=1900, max=2024)])
    description = TextAreaField('Description', validators=[DataRequired()])
    rating = IntegerField('Rating', validators=[DataRequired(), NumberRange(min=1, max=10)])
    ranking = IntegerField('Ranking', validators=[DataRequired(), NumberRange(min=1, max=10)])
    review = TextAreaField('Review', validators=[DataRequired(), length(min=2, max=200)])
    img_url = StringField('Image URL', validators=[DataRequired(), URL()])

    submit = SubmitField('Add')


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    movies = db.session.execute(db.session.query(Movie)).scalars()

    return render_template("index.html", movies=movies.all())


@app.get("/add")
def add_page():
    add_form = MovieForm(meta={'csrf': False})

    return render_template("add.html", add_form=add_form)


@app.post("/add")
def add_movie():
    add_form = MovieForm(meta={'csrf': False})

    title = add_form.title.data
    year = add_form.year.data
    description = add_form.description.data
    rating = add_form.rating.data
    ranking = add_form.ranking.data
    review = add_form.review.data
    img_url = add_form.img_url.data

    if add_form.validate_on_submit():
        db.session.add(
            Movie(title=title, year=year, description=description, rating=rating, ranking=ranking, review=review,
                  img_url=img_url))

        db.session.commit()

        redirect(url_for("home"))
    else:
        print("Forms is invalid", add_form.errors)

    return render_template("add.html", add_form=add_form)


@app.get("/edit/<int:movie_id>")
def edit_page(movie_id: int):
    print("movie_id", movie_id)

    movie = db.session.query(Movie).get(movie_id)

    edit_form = MovieForm(meta={'csrf': False})

    edit_form.title.data = movie.title
    edit_form.year.data = movie.year
    edit_form.description.data = movie.description
    edit_form.rating.data = movie.rating
    edit_form.ranking.data = movie.ranking
    edit_form.review.data = movie.review
    edit_form.img_url.data = movie.img_url

    return render_template("edit.html", edit_form=edit_form)


@app.post("/edit/<int:movie_id>")
def edit(movie_id: int):
    edit_form = MovieForm(meta={'csrf': False})

    new_title = edit_form.title.data
    new_year = edit_form.year.data
    new_description = edit_form.description.data
    new_rating = edit_form.rating.data
    new_ranking = edit_form.ranking.data
    new_review = edit_form.review.data
    new_img_url = edit_form.img_url.data

    target_movie = db.session.query(Movie).get(movie_id)

    movie_has_changes = False

    if new_title != target_movie.title:
        movie_has_changes = True
        target_movie.title = new_title

    if new_year != target_movie.year:
        movie_has_changes = True
        target_movie.year = new_year

    if new_description != target_movie.description:
        movie_has_changes = True
        target_movie.description = new_description

    if new_rating != target_movie.rating:
        movie_has_changes = True
        target_movie.rating = new_rating

    if new_ranking != target_movie.ranking:
        movie_has_changes = True
        target_movie.ranking = new_ranking

    if new_review != target_movie.review:
        movie_has_changes = True
        target_movie.review = new_review

    if new_img_url != target_movie.img_url:
        movie_has_changes = True
        target_movie.img_url = new_img_url

    if movie_has_changes:
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", edit_form=edit_form)


@app.get("/delete/<int:movie_id>")
def delete(movie_id: int):
    target_movie = db.session.query(Movie).get(movie_id)

    db.session.delete(target_movie)

    db.session.commit()

    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True, port=8080)
