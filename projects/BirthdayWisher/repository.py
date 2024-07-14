import pandas


class Repository:
    """Class to handle the existing birthdays"""

    def __init__(self, path) -> None:
        self.path = path

        self.content = None

        self.initialize()

    def initialize(self):
        """Try to read the initial data"""
        try:
            self.content = pandas.read_csv(self.path)
        except FileNotFoundError:
            print(f"FileNotFount, no file at {self.path}")
            self.content = pandas.DataFrame(
                {"name": [], "email": [], "year": [], "month": [], "day": []}
            )
            self.save()

    def active_birthdays(self, date):
        """Get all the people with a birthday today"""
        current_day = date.day
        current_month = date.month

        return self.content.loc[
            (current_day == self.content.day) & (current_month == self.content.month)
        ]

    def save(self):
        """Save the existing data to the"""
        self.content.to_csv(self.path, index=False)
