from datetime import datetime
from os import getenv

from dotenv import load_dotenv

from alphavantage_client import AlphaVantageClient
from messenger import Messenger
from news_client import NewsClient

load_dotenv()

STOCK_API_KEY = getenv("STOCK_API_KEY")
NEWS_API_KEY = getenv("NEWS_API_KEY")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
COMPANY_SHORTNAME = "tesla"

STOCK_DIFF_THRESHOLD = 1

stock_client = AlphaVantageClient(api_key=STOCK_API_KEY)
news_client = NewsClient(api_key=NEWS_API_KEY)

messenger = Messenger()


def get_price_diff():
    stock_response = stock_client.get_prices(stock=STOCK)
    stock_prices = stock_response["Time Series (Daily)"]
    stock_list = [value for (keuy, value) in stock_prices.items()]

    yesterday_data = stock_list[0]
    yesterday_price = float(yesterday_data["4. close"])

    before_yesterday_data = stock_list[1]
    before_yesterday_price = float(before_yesterday_data["4. close"])

    price_diff = yesterday_price - before_yesterday_price

    return (price_diff / yesterday_price) * 100


def get_stock_news() -> dict:
    today_str = f"{datetime.now().strftime('%Y-%m-')}01"

    news_response = news_client.get_news(from_=today_str, q=COMPANY_SHORTNAME)
    news_articles = news_response["articles"]
    return news_articles[:2]


stock_diff = get_price_diff()

if abs(stock_diff) > STOCK_DIFF_THRESHOLD:
    recent_articles = get_stock_news()

    for article in recent_articles:
        messages = messenger.create_message(stock=STOCK, diff=get_price_diff(), headline=article["title"],
                                            brief=article["description"])

        # send the message
        print(messages)
else:
    print("Not enough diff to trigger teh alert")
