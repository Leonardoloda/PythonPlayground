from os import urandom

from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap5

from add_coffee_form import AddCoffeeForm
from coffee import Coffee
from constants import *
from datasource import Datasource

datasource = Datasource(path=CAFES_FILE_PATH)
app = Flask(__name__)

Bootstrap5(app)

SECRET_KEY = urandom(24)
app.config['SECRET_KEY'] = SECRET_KEY
app.secret_key = SECRET_KEY


@app.get("/home")
def home():
    return render_template("index.html")


@app.get("/cafes")
def cafes():
    data = datasource.get_data()

    return render_template("cafes.html", data=data)


@app.get("/add")
def create_cafe():
    coffee_form = AddCoffeeForm()

    return render_template("add.html", form=coffee_form)


@app.post("/add")
def add_cafe():
    coffee_form = AddCoffeeForm()

    if not coffee_form.validate_on_submit():
        return render_template("add.html", form=coffee_form)

    name = coffee_form.name.data
    location = coffee_form.location.data
    opening = coffee_form.open_time.data
    closing = coffee_form.close_time.data
    coffee = coffee_form.coffee.data
    wifi = coffee_form.wifi.data
    power = coffee_form.power.data

    cafe = Coffee(name=name, location=location, opening=opening, closing=closing, coffee=coffee, wifi=wifi, power=power)

    datasource.add_cafe(cafe)

    return redirect(url_for('cafes'))


@app.errorhandler(404)
def not_fount(_):
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True, port=PORT)
