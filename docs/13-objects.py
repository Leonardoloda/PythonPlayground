# OOP

from random import randint
from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()

tim.shape("turtle")
tim.color("red")

x = 0
angle = 1

while x < 100:
    tim.left(randint(0, 180))
    tim.forward(100)

    x += 1
    angle += 1 / 2

# screen.exitonclick()

# You can use pypy to search for external librarire
from prettytable import PrettyTable

# Allows us to create a pretty table for ascii
table = PrettyTable()

table.field_names = ["Pokemon", "Type"]
table.add_row(["Pikachu", "electric"])
table.add_row(["Charmander", "fire"])

print(table.get_string())
