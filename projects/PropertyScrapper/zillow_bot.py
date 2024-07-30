from bs4 import BeautifulSoup

from property import Property


class ZillowBot:
    def __init__(self, html: str) -> None:
        self.soup = BeautifulSoup(html, 'html.parser')

    @staticmethod
    def process_property(card: BeautifulSoup) -> str:
        price_tag = card.select_one("span[data-test='property-card-price']")
        address_tag = card.select_one('address[data-test="property-card-addr"]')
        url_tag = card.select_one('a[data-test="property-card-link"]')

        price = price_tag.text.strip()
        address = address_tag.text.strip()
        url = url_tag.get('href')

        return Property(address=address, price=price, url=url)

    def fetch_properties(self) -> list:
        property_cards = self.soup.select("article[data-test='property-card']")

        properties = []

        for property_card in property_cards:
            properties.append(self.process_property(property_card))

        return properties
