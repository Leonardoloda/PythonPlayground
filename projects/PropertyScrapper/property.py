class Property:
    def __init__(self, address: str, price: str, url: str) -> None:
        self._address = address
        self._price = price
        self._url = url

    @property
    def address(self):
        return self._address

    @property
    def price(self):
        return self._price

    @property
    def url(self):
        return self._url

    @address.setter
    def address(self, address):
        self._address = address

    @price.setter
    def price(self, price):
        self._price = price

    @url.setter
    def url(self, url):
        self._url = url

    def __str__(self):
        return f"Property(price: {self.price}, url: {self.url}, address: {self.address})"
