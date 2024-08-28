class Square:
    def __init__(self, row: int, col: int, value: str):
        self._row = row
        self._col = col
        self._value = value

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value: str):
        self._value = value

    def __str__(self):
        return self._value

    def __repr__(self):
        return self._value
