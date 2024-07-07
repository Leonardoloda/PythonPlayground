from turtle import Turtle

from constants import Constants


class Racket(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=Constants.RACKET_SIZE)
        self.hideturtle()

    def draw(self, x):
        self.goto(x, y=0)
        self.showturtle()

    def up(self):
        self.move_vertically(self.ycor() + Constants.RACKET_SPEED)

    def down(self):
        self.move_vertically(self.ycor() - Constants.RACKET_SPEED)

    def move_vertically(self, y):
        if y >= (Constants.SCREEN_HEIGHT / 2) - 50:
            self.sety(Constants.SCREEN_HEIGHT / 2 - 50)
        elif y <= -(Constants.SCREEN_HEIGHT / 2) + 50:
            self.sety(-Constants.SCREEN_HEIGHT / 2 + 55)
        else:
            self.sety(y)
