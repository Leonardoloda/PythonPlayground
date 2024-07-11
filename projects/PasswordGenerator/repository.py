from os import path

import pandas


class Repository:
    def __init__(self, path):
        self.path = path
        self.content = None

        self.initialize()

    def initialize(self):
        if path.exists(self.path):
            self.content = pandas.read_csv(self.path)
        else:
            self.content = pandas.DataFrame({
                "websites": [],
                "passwords": [],
                "emails": []
            })

    def add_website(self, website, email, password):
        self.content.loc[-1] = [website, password, email]
        self.content.index = self.content.index + 1
        self.content = self.content.sort_index()

        self.content.to_csv(self.path)
