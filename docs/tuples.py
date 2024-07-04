# you can import specific things
from random import choices, choice
from turtle import Turtle, Screen

# but you can also import everything
# from turtle import *

# You can also use alias to import
# import turtle as T
# from turtle import Turtle as t

turtle = Turtle()
screen = Screen()

screen.colormode(255)

turtle.shape(name="circle")
turtle.color("red", "DarkGoldenrod")
turtle.speed(0)


class Painter:
    def __init__(self, turtle):
        self.turtle = turtle

    def square(self, width=100):
        for i in range(4):
            self.turtle.forward(width)
            self.turtle.left(90)

    def toggle_pen(self):
        if self.turtle.pen()['pendown']:
            self.turtle.penup()
        else:
            self.turtle.pendown()

    def dashed_line(self, size, gap=10):
        self.toggle_pen()

        for i in range(0, size, gap):
            self.toggle_pen()
            self.turtle.forward(gap)

        self.turtle.pendown()

    def change_color(self, color="black"):
        self.turtle.color(color)

    def polygon(self, size, sides):
        for i in range(sides):
            self.turtle.forward(size)
            self.turtle.left(360 / sides)
            self.random_color()

    def polygons(self, size=100, max_sides=4):
        if max_sides < 4:
            print("Not enough sides")

        for i in range(4, max_sides + 1):
            self.polygon(size, i)

    def random_color(self):
        self.turtle.color(choices(range(0, 255), k=3))

    def random_direction(self):
        return choice([self.turtle.right, self.turtle.left])

    def set_stroke(self, stroke=10):
        self.turtle.width(stroke)

    def random_walk(self):
        self.set_stroke(10)
        while True:
            self.random_direction()(90)
            self.turtle.forward(10)
            self.random_color()

    def circle(self, radius, extent=None, steps=None):
        self.turtle.circle(radius, extent, steps)

    def spirograph(self, radius=100, steps=10):
        self.random_color()
        for i in range(0, 360, steps):
            self.turtle.setheading(i)
            self.circle(radius)


print()
painter = Painter(turtle)

# painter.square()
# painter.dashed_line(100, 10)
# painter.polygons(size=100, max_sides=5)
# painter.random_walk()

painter.spirograph(radius=200, steps=5)

screen.exitonclick()

# Python supports tuples that are inmutable lists
tuple = (1, 2, 3)

# Therefo0re you cant change value
# tuple[0] = 2
