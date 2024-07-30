from os import getenv
from time import sleep

from constants import LOGIN_TIMEOUT
from dotenv import load_dotenv
from insta_bot import InstaBot
from selenium import webdriver

load_dotenv()

INSTAGRAM_USER = getenv("INSTAGRAM_USER")
INSTAGRAM_PASSWORD = getenv("INSTAGRAM_PASSWORD")
INSTAGRAM_URL = getenv("INSTAGRAM_URL")
INSTAGRAM_PROFILE = getenv("INSTAGRAM_PROFILE")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


chrome = webdriver.Chrome(options=chrome_options)
chrome.maximize_window()
chrome.implicitly_wait(1)

insta_bot = InstaBot(browser=chrome)

insta_bot.go_to(INSTAGRAM_URL)
insta_bot.login(user=INSTAGRAM_USER, password=INSTAGRAM_PASSWORD)

sleep(LOGIN_TIMEOUT)


while not input("Are you done with verification? y/n ") == "y":
    pass

try:
    insta_bot.dissmiss_popup()
except Exception as e:
    print("No popup present")

insta_bot.go_to(INSTAGRAM_PROFILE)

sleep(1)
insta_bot.follow_followers()
