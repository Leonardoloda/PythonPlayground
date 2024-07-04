from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

current_angle = 0


class MagicBoard:
    def __init__(self, turtle, screen):
        self.turtle = turtle
        self.screen = screen
        self.current_angle = 0

    def move_forward(self):
        turtle.forward(10)

    def move_backward(self):
        turtle.backward(10)

    def turn_left(self):
        self.current_angle += 10
        turtle.setheading(self.current_angle)

    def turn_right(self):
        self.current_angle -= 10
        turtle.setheading(self.current_angle)

    def reset(self):
        turtle.clear()
        turtle.penup()
        turtle.home()
        turtle.pendown()


board = MagicBoard(turtle, screen)

screen.onkey(key="Up", fun=board.move_forward)
screen.onkey(key="Down", fun=board.move_backward)
screen.onkey(key="Left", fun=board.turn_left)
screen.onkey(key="Right", fun=board.turn_right)
screen.onkey(key="c", fun=board.turn_left)

screen.listen()

screen.exitonclick()
