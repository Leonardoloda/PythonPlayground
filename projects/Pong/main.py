from turtle import Screen

from ball import Ball
from constants import Constants
from racket import Racket
from score import Score

screen = Screen()

screen.setup(width=Constants.SCREEN_WIDTH, height=Constants.SCREEN_HEIGHT)
screen.title(titlestring="Pong")
screen.tracer(0)
screen.bgcolor("black")

screen.listen()

left_racket = Racket()
right_racket = Racket()

left_score = Score()
right_score = Score()

ball = Ball()

left_racket.draw(x=Constants.LEFT_PADDLE_X)
right_racket.draw(x=Constants.RIGHT_PADDLE_X - 10)

left_score.align_score(x=Constants.LEFT_SCORE_X, y=Constants.LEFT_SCORE_Y)
right_score.align_score(x=Constants.RIGHT_SCORE_X, y=Constants.RIGHT_SCORE_Y)

screen.onkey(key="Up", fun=left_racket.up)
screen.onkey(key="Down", fun=left_racket.down)

left_score.show_score()
right_score.show_score()

while True:
    screen.update()
    ball.move()

    ball_y = ball.ycor()
    ball_x = ball.xcor()

    left_racket_y = left_racket.ycor()
    left_racket_top_y = left_racket_y + Constants.RACKET_HEIGHT / 2
    left_racket_bottom_y = left_racket_y - Constants.RACKET_HEIGHT / 2

    right_racket_y = right_racket.ycor()
    right_racket_top_y = right_racket_y + Constants.RACKET_HEIGHT / 2
    right_racket_bottom_y = right_racket_y - Constants.RACKET_HEIGHT / 2

    if ball_x == Constants.LEFT_PADDLE_AXIS + Constants.BALL_RADIUS:
        print(left_racket_bottom_y, ball_y, left_racket_top_y)

    if ((ball_x == Constants.RIGHT_PADDLE_AXIS - Constants.BALL_RADIUS) and
            right_racket_top_y > ball_y > right_racket_bottom_y):
        ball.bounce_x()

    if ((ball_x == Constants.LEFT_PADDLE_AXIS + Constants.BALL_RADIUS) and
            left_racket_bottom_y < ball_y < left_racket_top_y):
        print("Allo")
        ball.bounce_x()

    if ball_x == Constants.LEFT_HALF:
        ball.reset()
        left_score.update_score()

    if ball_x == Constants.RIGHT_HALF:
        ball.reset()
        right_score.update_score()

    right_racket.move_vertically(y=ball_y)

screen.exitonclick()
