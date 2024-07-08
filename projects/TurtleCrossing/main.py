"""Control the speexd of the game"""

from time import sleep

from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.onkey(key="w", fun=player.advance)
screen.onkey(key="s", fun=player.retreat)
screen.onkey(key="a", fun=player.move_left)
screen.onkey(key="d", fun=player.move_right)

screen.listen()

game_is_on = True

while game_is_on:
    sleep(0.1)
    screen.update()

    player_x = player.xcor()
    player_y = player.ycor()

    if player_y > 200:
        scoreboard.next_level()
        player.reset()

    car_manager.create_car()
    car_manager.move_cars()

    if car_manager.has_collided(x=player_x, y=player_y):
        game_is_on = False

scoreboard.game_over()
screen.exitonclick()
