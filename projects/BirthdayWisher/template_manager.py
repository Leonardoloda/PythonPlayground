from random import choice
from os import listdir


class TemplateManager:
    """Class to handle the files"""

    def __init__(self, templates_path) -> None:
        self.templates_path = templates_path

    def get_random_template(self):
        """Returns a random template path"""
        template_path = f"{self.templates_path}{choice(listdir(self.templates_path))}"
        try:
            with open(template_path, mode="r", encoding="utf8") as file:
                return file.read()
        except FileNotFoundError:
            print("There's not a configured template")
            return "Happy Birthday [NAME]"
