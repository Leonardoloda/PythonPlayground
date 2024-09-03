from datetime import datetime
from os import urandom, getenv
from uuid import uuid4

from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

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


class Note(db.Model):
    __tablename__ = 'notes'

    id: Mapped[str] = mapped_column(String, primary_key=True, default=uuid4().hex)
    text: Mapped[str] = mapped_column(String(250), nullable=False)
    created_at: Mapped[str] = mapped_column(DateTime, nullable=False, default=datetime.now())


with app.app_context():
    db.create_all()


@app.get("/")
def home():
    return redirect(url_for('create'))


@app.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        content = request.form['content']

        note = Note(id=uuid4().hex, text=content)

        db.session.add(note)
        db.session.commit()

        return render_template("create.html", link=note.id)

    return render_template('create.html')


@app.get("/note/<todo_id>")
def share(todo_id: str):
    note = Note.query.filter_by(id=todo_id).first()

    db.session.delete(note)
    db.session.commit()

    return render_template("note.html", content=note.text)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
