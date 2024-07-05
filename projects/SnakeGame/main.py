from turtle import Screen

from food import Food
from score import Score
from snake import Snake

screen = Screen()

WIDTH = 800
HEIGHT = 800
MARGIN = 25
TITLE = "Snake Game"
BG_COLOR = "#1e1e1e"
BODY_PART_SIZE = 20

PLAYABLE_WIDTH = WIDTH - (MARGIN * 2)
PLAYABLE_HEIGHT = HEIGHT - (MARGIN * 2)

screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor(BG_COLOR)
screen.title(titlestring=TITLE)
screen.tracer(n=0)

snake = Snake()
food = Food()
score = Score()

screen.update()

screen.listen()

screen.onkey(key="Right", fun=snake.turn_east)
screen.onkey(key="Up", fun=snake.turn_north)
screen.onkey(key="Left", fun=snake.turn_west)
screen.onkey(key="Down", fun=snake.turn_south)

score.align_score(0, HEIGHT / 2 - 50)
score.show_score()

still_alive = True

while still_alive:
    snake.move_forward()
    screen.update()

    if snake.head.distance(food) < 15:
        print("Yummy")
        snake.grow_body()
        score.update_score()
        food.relocate(WIDTH, HEIGHT)

    if (snake.head.xcor() > PLAYABLE_WIDTH / 2
            or snake.head.xcor() < -PLAYABLE_WIDTH / 2
            or snake.head.ycor() < -PLAYABLE_HEIGHT / 2
            or snake.head.ycor() > PLAYABLE_HEIGHT / 2):
        score.game_over()
        still_alive = False

    for part in snake.body[2:]:
        if snake.head.distance(part) < BODY_PART_SIZE:
            score.game_over()
            still_alive = False

screen.exitonclick()
