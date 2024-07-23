from constants import *
from website_client import WebsiteClient
from website_scraper import WebsiteScraper

print("""
Welcome to the news scrapper, here you'll get the most upvoted news
""")

client = WebsiteClient(url=NEWS_WEBSITE)

html = client.get_website()

scraper = WebsiteScraper(html)

news = scraper.get_all_news()

print(f"{len(news)} news fount, here's the top rated article")

news.sort(key=lambda article: article["score"], reverse=True)

print(f"{news[0]['title']} read more here: {news[0]["link"]}")
