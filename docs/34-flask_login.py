from os import urandom

from flask import Flask, render_template, request, url_for, redirect
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# To set up Flask login, you need to set up a login manager
login_manager = LoginManager()

login_manager.init_app(app)

# To be able to use it, you  need to set up a secret key
app.config['SECRET_KEY'] = urandom(32)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(model_class=Base)
db.init_app(app)


# You need to have an user class wth certain properties, but it can be extended from the UserMixin
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(250), nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


# You need to set up a user_loader whch is afunction that returns the instance of anu ser baseed on the id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        # You can use any library to securely store your password in a database
        secure_password = generate_password_hash(password, method='pbkdf2', salt_length=8)

        user = User(username=username, password=secure_password)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template("flask_login/register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        user = db.session.query(User).where(User.username == username).first()

        is_valid_password = check_password_hash(user.password, password)

        if is_valid_password:
            login_user(user)
            return redirect(url_for('profile'))

    return render_template("flask_login/login.html")


# Now you have the login_required decorator to protect routes
@app.get("/profile")
@login_required
def profile():
    # by using teh current_user, you can access the info for an authenticated user
    return render_template("flask_login/profile.html", username=current_user.username)


@app.get("/logout")
@login_required
def logout():
    # You can just call logout to end a user's session
    logout_user()

    return redirect(url_for('login'))


app.run(port=8080, debug=True)
