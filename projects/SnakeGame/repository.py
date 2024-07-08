class Repository:
    def __init__(self, path):
        self.path = path

    def add_highest_score(self, score):
        with open(self.path, "w") as file:
            print("Score", score)
            file.write(str(score))

    def get_highest_score(self):
        with open(self.path, "r") as file:
            return int(file.read()) if file.read() else 0
