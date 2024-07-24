from amazon_scrapper import AmazonScrapper
from constants import *
from email_client import EmailClient


class PriceWatcher:
    SUBJECT_TEMPLATE = "Your {product} is at a new record low"
    BODY_TEMPLATE = "{product} is currently at ${price}"

    def __init__(self, email_client: EmailClient, scraper: AmazonScrapper) -> None:
        self._email_client = email_client
        self._scraper = scraper

    def build_subject(self, product_name: str) -> str:
        return self.SUBJECT_TEMPLATE.format(product=product_name)

    def build_body(self, product_name: str, price: float) -> str:
        return self.BODY_TEMPLATE.format(product=product_name, price=price)

    def track_price(self):
        current_price = self._scraper.get_price()
        product_name = self._scraper.get_title()

        if TARGET_PRICE > current_price:
            subject = self.build_subject(product_name=product_name)
            body = self.build_body(product_name=product_name, price=current_price)

            self._email_client.send_email(email=ALERT_EMAIL, subject=subject, body=body)
        else:
            print("Price is currently expensive, try it next time")
