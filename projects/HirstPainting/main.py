from turtle import Turtle, Screen

from painter import Painter

turtle = Turtle()
screen = Screen()

screen.colormode(255)

painter = Painter(turtle)

PAINTING_WIDTH = 400
PAINTING_HEIGHT = 400

painter.paint_grid(width=PAINTING_WIDTH, height=PAINTING_HEIGHT, step=50)

screen.exitonclick()
