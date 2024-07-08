""" Module to be able to render on screen """

from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Scoreboard class to display the score"""

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def update_scoreboard(self):
        """Update the scoreboard"""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def next_level(self):
        """Increase the level"""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Display the game over"""
        self.goto(0, 0)
        self.write("Game over", align="center", font=FONT)
