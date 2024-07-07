from turtle import Turtle

from constants import Constants


class Ball(Turtle):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')

        self.x = x
        self.y = y

        self.x_dir = Constants.BALL_SPEED
        self.y_dir = Constants.BALL_SPEED

    def reset(self):
        self.x = 0
        self.y = 0

        self.goto(self.x, self.y)

    def bounce_x(self):
        self.x_dir = - self.x_dir

    def bounce_y(self):
        self.y_dir = - self.y_dir

    def move(self):
        self.y += self.y_dir
        self.x += self.x_dir

        self.goto(self.x, self.y)

        if not Constants.BOTTOM_HALF + Constants.BALL_RADIUS <= self.y <= Constants.TOP_HALF - Constants.BALL_RADIUS:
            self.bounce_y()
