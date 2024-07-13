from random import randint

import pandas


class CSVRepository:
    def __init__(self, path):
        self.path = path
        self.content = None

        self.initialize()

    def initialize(self):
        try:
            self.content = pandas.read_csv(self.path)
            if "Memorized" not in self.content:
                self.content.insert(2, "Memorized", False, allow_duplicates=True)

        except FileNotFoundError:
            self.content = pandas.DataFrame({
                "French": [],
                "English": [],
                "Memorized": []
            })
        finally:
            self.save()

    def save(self):
        self.content.to_csv(self.path, index=False)

    def check_word(self, word):
        self.content.loc[self.content['French'] == word, 'Memorized'] = True

        self.save()

    def get_word(self):
        try:
            return self.content.iloc[randint(0, len(self.content) - 1)]
        except IndexError:
            print("Out of words")
            return None
