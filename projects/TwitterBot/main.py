from os import getenv

from dotenv import load_dotenv
from selenium import webdriver

from constants import *
from speedtest_bot import SpeedBot
from twitter_bot import TwitterBot

load_dotenv()

TWITTER_USERNAME = getenv('TWITTER_USERNAME')
TWITTER_PASSWORD = getenv('TWITTER_PASSWORD')
TWITTER_EMAIL = getenv('TWITTER_EMAIL')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

chrome = webdriver.Chrome(options=chrome_options)
chrome.maximize_window()
chrome.implicitly_wait(5)

speed_bot = SpeedBot(driver=chrome)
twitter_bot = TwitterBot(driver=chrome)

current_speed = speed_bot.test_speed()

print(f'Current speed: {current_speed}')

logged_in = False
try:
    twitter_bot.login(user=TWITTER_USERNAME, password=TWITTER_PASSWORD, email=TWITTER_EMAIL)
    logged_in = True
except Exception as e:
    print(e)
    logged_in = False

if logged_in:
    twitter_bot.tweet(TWEET_TEMPLATE.format(speed=current_speed))
else:
    print("twitter login failed, please try again")
