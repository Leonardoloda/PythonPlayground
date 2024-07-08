from turtle import Turtle
from random import choice, randrange
from math import fabs

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """Car manager class to control the cars"""

    def __init__(self):
        self.cars = []

    def create_car(self):
        """Create a car"""
        options = [True, False]
        create = choice(options)

        if not create:
            return

        new_car = Turtle()
        new_car.shape("square")
        new_car.color(choice(COLORS))
        new_car.shapesize(stretch_len=2)
        new_car.penup()
        new_car.goto(x=290, y=randrange(-200, 200, 50))
        new_car.setheading(180)

        self.cars.append(new_car)

    def move_cars(self):
        """Move the cars along"""
        for car in self.cars:
            if car.xcor() < -320:
                car.hideturtle()
                self.cars.remove(car)
                continue

            car.forward(MOVE_INCREMENT)

    def has_collided(self, x, y):
        """Checks if it has crashed to anycar"""

        crash_distance_x = 20
        crash_distance_y = 40

        for car in self.cars:
            car_x = car.xcor()
            car_y = car.ycor()

            if (
                fabs(car_y - y) < crash_distance_y
                and fabs(car_x - x) < crash_distance_x
            ):
                return True

        return False
