from bs4 import BeautifulSoup


class AmazonScrapper:
    def __init__(self, html: str) -> None:
        self.soup = BeautifulSoup(html, 'html.parser')

    def get_price(self) -> float:
        whole_tags = self.soup.select(".a-price-whole")
        decimal_tags = self.soup.select(".a-price-fraction")

        whole_tag = whole_tags[1]
        decimal_tag = decimal_tags[1]

        whole = whole_tag.text.strip()
        decimal = decimal_tag.text.strip()

        price_str = f"{whole}{decimal}"
        price = float(price_str)

        return price

    def get_title(self) -> str:
        title_tag = self.soup.select_one("#productTitle")

        return title_tag.text.strip()
