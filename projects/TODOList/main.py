from os import urandom, getenv

from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from constants import PENDING, COMPLETED
from forms import CreateTODOForm

load_dotenv()

SECRET_KEY = urandom(32)
DATABASE_URL = getenv('DATABASE_URL')

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
bootstrap = Bootstrap5(app)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Todo(db.Model):
    __tablename__ = 'todos'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    status: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.get("/")
def home():
    todos = db.session.query(Todo).all()

    return render_template('index.html', todos=todos)


@app.route("/add", methods=['GET', 'POST'])
def add():
    create_form = CreateTODOForm(meta={
        "csrf": False
    })

    if request.method == "POST":
        description = request.form.get("description")

        todo = Todo(description=description, status=PENDING)

        db.session.add(todo)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('add.html', form=create_form)


@app.route("/delete/<int:todo_id>")
def delete(todo_id: int):
    todo = Todo.query.get(todo_id)

    todo.status = COMPLETED

    db.session.add(todo)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(port=8080, debug=True)
