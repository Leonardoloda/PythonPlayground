from turtle import Turtle


class Score(Turtle):
    def __init__(self, repository):
        super().__init__()

        self.repository = repository
        self.points = 0
        self.highest_score = 0

        self.color("white")
        self.penup()
        self.hideturtle()

        self.get_score()

    def get_score(self):
        self.highest_score = self.repository.get_highest_score()

    def align_score(self, x, y):
        self.goto(x, y)

    def show_score(self):
        self.write(f'Score: {self.points} Highest Score {self.highest_score}', align='center',
                   font=('Arial', 16, 'bold'))

    def update_score(self):
        self.clear()
        self.show_score()

    def reset(self):
        if self.points > self.highest_score:
            self.highest_score = self.points
            self.repository.add_highest_score(self.points)
            
        self.points = 0
        self.update_score()

    def add_point(self):
        self.points += 1
        self.update_score()
