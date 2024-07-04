from math import floor
from random import randint
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

WIDTH = 1_000
HEIGHT = 800
CONTESTANTS = ["red", "blue", "green", "yellow", "black"]
DISTANCE = 100

screen.setup(width=WIDTH, height=HEIGHT)

bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")

turtles = []
offset = -floor(len(CONTESTANTS) / 2) * DISTANCE

for color in CONTESTANTS:
    new_turtle = Turtle(shape="turtle")

    new_turtle.penup()
    new_turtle.teleport(x=-(WIDTH - 50) / 2, y=offset)
    new_turtle.speed(randint(0, 5))
    new_turtle.color(color)

    offset += DISTANCE
    turtles.append(new_turtle)

is_race_on = True

while is_race_on:
    for turtle in turtles:
        turtle.forward(randint(5, 10))

        if turtle.xcor() > WIDTH / 2:
            winner = turtle.pencolor()
            is_race_on = False

print(f"Turtle {winner} has won!")

if winner == bet:
    print("You've bet for the right turtle, congrats")
else:
    print(f"You've bet for the {bet} turtle, F")

screen.exitonclick()
