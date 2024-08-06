class Coffee:
    def __init__(self, name: str, location: str, opening: str, closing: str, coffee: str, wifi: str,
                 power: str) -> None:
        self._name = name
        self._location = location
        self._opening = opening
        self._closing = closing
        self._coffee = coffee
        self._wifi = wifi
        self._power = power

    def to_row(self) -> list:
        return [self._name, self._location, self._opening, self._closing, self._coffee, self._wifi, self._power]
