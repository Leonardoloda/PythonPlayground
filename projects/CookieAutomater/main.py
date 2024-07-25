from time import sleep

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By

URL = 'https://orteil.dashnet.org/cookieclicker/'
CLICK_RATE = 0
LOAD_TIME = 3

driver = webdriver.Chrome()

driver.get(URL)


def start_game():
    cookie_button = driver.find_element(By.ID, "bigCookie")
    cookies_tag = driver.find_element(By.ID, "cookies")

    while True:
        available_levels = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")

        if len(available_levels) > 0:
            available_levels[-1].click()

        available_updates = driver.find_elements(By.CSS_SELECTOR, ".crate.upgrade.enabled")

        if len(available_updates) > 0:
            available_updates[-1].click()

        cookie_button.click()

        sleep(CLICK_RATE)


try:
    start_game()
except ElementClickInterceptedException:
    print("Welcome message fount, setting language")
    english_option = driver.find_element(By.ID, "langSelect-EN")

    english_option.click()

    sleep(LOAD_TIME)
finally:
    start_game()
