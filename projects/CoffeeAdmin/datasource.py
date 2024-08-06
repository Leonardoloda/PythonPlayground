import pandas

from coffee import Coffee


class Datasource:
    def __init__(self, path: str) -> None:
        self._path = path
        self.data = pandas.DataFrame()

        self.read_csv()

    def read_csv(self):
        self.data = pandas.read_csv(self._path)

    def get_data(self):
        return self.data.to_dict('tight')

    def save_data(self):
        return self.data.to_csv(self._path, index=False)

    def add_cafe(self, cafe: Coffee):
        self.data.loc[-1] = cafe.to_row()  # adding a row
        self.data.index = self.data.index + 1  # shifting index
        self.data = self.data.sort_index()
