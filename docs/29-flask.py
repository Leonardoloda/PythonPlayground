from os import urandom

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length

app = Flask(__name__)

# flask boostrap allows you to create parent templates with bootstrap loaded
bootstrap = Bootstrap5(app)


def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"

    return wrapper


def underline(func):
    def wrapper():
        return "<u>" + func() + "</u>"

    return wrapper


def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"

    return wrapper


@app.route("/")
@bold
@underline
@italic
def hello_world():
    return "<p>Hello, World!</p>"


# You can also receive path or url parameters by adding them with a <>
@app.route("/hello/<user>")
def hello_user(user):
    return f"<p>Hello, {user}!</p>"


# You can also parse those values
@app.route("/hello/multiple/<int:times>")
def hello_multiple_times(times):
    return [f"<p>Hello, {times}!</p>" for _ in range(times)]


# You can use debug mode to check errors
@app.route("/fail/<name>")
def fail(name):
    return f"<p>{name + 1}</p>"


# you can also use static files, but they need to be located in the template
@app.get("/static")
def static_files():
    return render_template("home.html")


@app.get("/form")
def form_page():
    return render_template("form.html")


@app.post("/submit")
def submit():
    # You can receive info from a form by using the request object from flask
    name = request.form["name"]

    return redirect(url_for("hello_user", user=name))


SECRET_KEY = urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


# You can use flask wtf to create forms with validatiosn
class LoginForm(FlaskForm):
    # YOu can pass the list of validator you wanna use
    user = StringField('user', validators=[DataRequired(), length(min=8, max=12)])
    password = PasswordField('password', validators=[DataRequired(), length(min=8, max=12)])
    login = SubmitField('Login', validators=[DataRequired()])


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    user = form.user.data
    password = form.password.data

    # Once you disable form validation in the browser, you can validate it here
    if form.validate_on_submit():
        return redirect(url_for('login_success'))
    else:
        return redirect(url_for('login_fail'))

    return render_template('login.html', form=form)


# You can use template inheritance to create multiple childs of a template
@app.get("/login/success")
def login_success():
    print("Login Success")
    return render_template("success.html")


@app.get("/login/fail")
def login_fail():
    print("fail")
    return render_template("fail.html")


# using bootsrap flask we can do the same but much simpler
@app.get('/login/bootstrap')
def login_bootstrap():
    form = LoginForm()

    return render_template("login_bootstrap.html", form=form)


# To be able to run flask applications, you need to export a flask_app env

# export FLASK_APP="29-flask.py"
# flask run

# You can enable debug mode to have hot reloading
# flask run --debug

# You can also run it using the __name__ attribute
if __name__ == "__main__":
    app.run(debug=True, port=8080)
