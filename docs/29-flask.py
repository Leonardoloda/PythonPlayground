from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


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


# To be able to run flask applications, you need to export a flask_app env

# export FLASK_APP="29-flask.py"
# flask run

# You can enable debug mode to have hot reloading
# flask run --debug

# You can also run it using the __name__ attribute
if __name__ == "__main__":
    app.run(debug=True, port=8080)
