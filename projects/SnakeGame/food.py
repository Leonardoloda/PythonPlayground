from random import randrange
from turtle import Turtle


class Food(Turtle):
    MARGIN = 10

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.speed("fastest")
        self.color("yellow")

    def relocate(self, width, height):
        horizontal_border = (-(width // 2 - self.MARGIN), (width // 2 - self.MARGIN))
        vertical_border = (-(height // 2 - self.MARGIN), (height // 2 - self.MARGIN))

        x = randrange(horizontal_border[0], horizontal_border[1])
        y = randrange(vertical_border[0], vertical_border[1])

        self.goto(x, y)
