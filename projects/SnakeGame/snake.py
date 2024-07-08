from time import sleep
from turtle import Turtle

BODY_PART_SIZE = 20


class Snake:
    INITIAL_LENGTH = 3
    RIGHT = 0
    UP = 90
    LEFT = 180
    DOWN = 270
    SPEED = 20

    def __init__(self):
        self.body = []
        self.head = None

        self.create_snake()

    def add_part(self):
        new_body = Turtle(shape="square")
        new_body.color("white")
        new_body.teleport(
            0 if len(self.body) == 0 else self.body[-1].xcor(),
            0 if len(self.body) == 0 else self.body[-1].ycor(),
        )
        new_body.penup()

        self.body.append(new_body)

    def create_snake(self):
        for _ in range(self.INITIAL_LENGTH):
            self.add_part()

        self.head = self.body[0]

    def move_body(self):
        for i in range(len(self.body) - 1, 0, -1):
            prev_x = self.body[i - 1].xcor()
            prev_y = self.body[i - 1].ycor()

            self.body[i].goto(prev_x, prev_y)

    def grow_body(self):
        self.add_part()

    def reset_body(self):
        for segment in self.body:
            segment.hideturtle()

        self.body = []
        self.haed = None

        self.create_snake()

    def move_forward(self):
        sleep(1 / 10)

        self.move_body()

        self.body[0].forward(self.SPEED)

    def turn_east(self):
        if self.body[0].heading() != self.LEFT:
            self.body[0].setheading(self.RIGHT)

    def turn_north(self):
        if self.body[0].heading() != self.DOWN:
            self.body[0].setheading(self.UP)

    def turn_west(self):
        if self.body[0].heading() != self.RIGHT:
            self.body[0].setheading(self.LEFT)

    def turn_south(self):
        if self.body[0].heading() != self.UP:
            self.body[0].setheading(self.DOWN)
