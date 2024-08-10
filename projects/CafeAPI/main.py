from random import choice

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }


with app.app_context():
    db.create_all()


# HTTP GET - Read Record
@app.get("/random")
def random():
    """Fetch a random cafe"""

    result = db.session.execute(db.select(Cafe))
    cafes = result.scalars().all()
    random_cafe = choice(cafes)

    return jsonify(
        cafe={
            "id": random_cafe.id,
            "name": random_cafe.name,
            "map_url": random_cafe.map_url,
            "img_url": random_cafe.img_url,
            "location": random_cafe.location,
        }
    )


@app.get("/cafes")
def all_cafes():
    """Fetch all the cafes"""
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()

    return [cafe.to_dict() for cafe in all_cafes]


@app.get("/search")
def cafe_by_location():
    """Searches for a cafe by the location in the query parameter"""

    location = request.args.get("location")

    result = db.session.execute(
        db.select(Cafe).where(Cafe.location.like(f"%{location}%"))
    )
    all_cafes = result.scalars().all()

    return [cafe.to_dict() for cafe in all_cafes]


@app.post("/cafe")
def add_cafe():
    """Adds a new cafe to the database"""

    name = request.form.get("name")
    map_url = request.form.get("map_url")
    img_url = request.form.get("img_url")
    location = request.form.get("location")
    has_sockets = request.form.get("has_sockets") == 1
    has_toilet = request.form.get("has_toilet") == 1
    has_wifi = request.form.get("has_wifi") == 1
    can_take_calls = request.form.get("can_take_calls") == 1
    seats = request.form.get("seats")
    coffee_price = request.form.get("coffee_price")

    new_cafe = Cafe(
        name=name,
        map_url=map_url,
        img_url=img_url,
        location=location,
        has_sockets=has_sockets,
        has_toilet=has_toilet,
        has_wifi=has_wifi,
        can_take_calls=can_take_calls,
        seats=seats,
        coffee_price=coffee_price,
    )

    db.session.add(new_cafe)

    db.session.commit()

    return jsonify(request.form)


@app.patch("/price/<int:cafe_id>")
def update_price(cafe_id):
    """Updates the price in a cafe by id"""
    price = request.form.get("price")

    target_cafe = db.session.query(Cafe).get(cafe_id)

    if not target_cafe:
        return jsonify({"error": "Couldn't find a Cafe with that Id"}), 404

    target_cafe.coffee_price = price

    db.session.commit()

    return "ok"


@app.delete("/cafe/<int:cafe_id>")
def delete_cafe(cafe_id):
    """Deletes a cafe by id as a path parameter"""

    target_cafe = db.session.query(Cafe).get(cafe_id)

    if not target_cafe:
        return jsonify({"error": "Couldn't find a Cafe with that Id"}), 404

    db.session.delete(target_cafe)

    db.session.commit()

    return "ok"


if __name__ == "__main__":
    app.run(debug=True, port=8080)
