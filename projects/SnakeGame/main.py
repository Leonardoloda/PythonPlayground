from turtle import Screen

from snake import Snake

screen = Screen()

WIDTH = 800
HEIGHT = 800
TITLE = "Snake Game"
BG_COLOR = "#1e1e1e"
BODY_PART_SIZE = 5

screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor(BG_COLOR)
screen.title(titlestring=TITLE)
screen.tracer(n=0)

snake = Snake()
screen.update()

screen.listen()

screen.onkey(key="Right", fun=snake.turn_east)
screen.onkey(key="Up", fun=snake.turn_north)
screen.onkey(key="Left", fun=snake.turn_west)
screen.onkey(key="Down", fun=snake.turn_south)

still_alive = True

while still_alive:
    snake.move_forward()
    screen.update()

    still_alive = snake.alive

screen.exitonclick()
