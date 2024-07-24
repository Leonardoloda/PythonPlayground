from os import getenv

from dotenv import load_dotenv

from amazon_client import AmazonClient
from amazon_scrapper import AmazonScrapper
from constants import *
from email_client import EmailClient
from price_watcher import PriceWatcher

load_dotenv()

EMAIL = getenv('EMAIL')
PASSWORD = getenv('PASSWORD')

client = AmazonClient(url=PRODUCT_URL)
email_client = EmailClient(email=EMAIL, password=PASSWORD)

html = client.fetch_website()

scraper = AmazonScrapper(html=html)

tracker = PriceWatcher(email_client=email_client, scraper=scraper)

tracker.track_price()
