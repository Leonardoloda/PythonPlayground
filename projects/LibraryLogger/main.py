from flask import Flask, render_template, redirect, url_for, request

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedColumn


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"

# initialize the app with the extension
db.init_app(app)


# You can use sql alchemy as an ORM to map your tables
class Book(db.Model):
    __tablename__ = "books"
    id: Mapped[int] = MappedColumn(primary_key=True)
    name: Mapped[str] = MappedColumn(unique=True)
    author: Mapped[str]
    rating: Mapped[float]

    def __repr__(self):
        return f'<Book {self.name}>'


# tell it to create the needed tables
with app.app_context():
    db.create_all()


@app.get("/books")
def books():
    db_books = db.session.execute(db.select(Book).order_by(Book.name)).scalars()

    # Now the books can be iterated through
    return render_template("index.html", books=db_books.all())


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form.get("name")
        author = request.form.get("author")
        rating = request.form.get("rating")

        db.session.add(Book(name=name, author=author, rating=rating))

        db.session.commit()

        return redirect(url_for("books"))

    return render_template("add.html")


@app.get("/books/<int:book_id>")
def delete_book(book_id):
    target_book = db.session.query(Book).get(book_id)

    db.session.delete(target_book)

    db.session.commit()

    return redirect(url_for("books"))


app.run(debug=True, port=8080)
