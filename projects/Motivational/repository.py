from random import choice


class Repository:
    """Class to handle the stored quotes in the file"""

    def __init__(self, path) -> None:
        self.path = path
        self.quotes = []

        self.initialize()

    def initialize(self):
        """Read the initial file"""
        try:
            with open(self.path, mode="r", encoding="utf8") as file:
                self.quotes = file.readlines()
        except FileNotFoundError:
            print("There's no quotes")
            exit()

    def get_random_quote(self):
        """Get a random quote"""
        return choice(self.quotes)
