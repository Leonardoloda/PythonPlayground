from turtle import Turtle

STARTING_POSITION = (0, -250)
MOVE_DISTANCE = 50
FINISH_LINE_Y = 250


class Player(Turtle):
    """Turtle class to control the player"""

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def advance(self):
        """Move the turtle along"""
        self.sety(self.ycor() + MOVE_DISTANCE)

    def retreat(self):
        """Move the turtle backwards"""
        self.sety(self.ycor() - MOVE_DISTANCE)

    def reset(self):
        """Reset the turtle position"""
        self.goto(STARTING_POSITION)

    def move_left(self):
        """Move the turtle to the left"""
        self.setx(self.xcor() - MOVE_DISTANCE)

    def move_right(self):
        """Move the turtle to the right"""
        self.setx(self.xcor() + MOVE_DISTANCE)
