from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()

        self.points = 0

    def align_score(self, x, y):
        self.goto(x, y)

    def show_score(self):
        self.write(f'Score: {self.points}', align='center', font=('Arial', 16, 'bold'))

    def update_score(self):
        self.clear()
        self.points += 1
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Arial', 16, 'bold'))
