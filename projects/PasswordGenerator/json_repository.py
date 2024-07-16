from json import load, dump


class JSONRepository:
    """Class to handle the JSON file"""

    def __init__(self, path):
        self.path = path

    def initialize(self):
        """Read the initial content or, if the file doesn't exist create a new one"""
        try:
            with open(self.path, mode="r", encoding="utf8") as file:
                pass
        except FileNotFoundError:
            with open(self.path, mode="w", encoding="utf8") as file:
                dump({}, file)

    def create_website(self, website, email, password):
        """Create a new record in the file for the password"""
        with open(self.path, mode="r+", encoding="utf8") as file:
            websites = load(file)

            websites.update({website: {"email": email, "password": password}})

            file.seek(0)

            dump(websites, file, indent=4)

    def search_website(self, website):
        """Gets a website by the key"""
        with open(self.path, mode="r+", encoding="utf8") as file:
            websites = load(file)

            return websites[website]
