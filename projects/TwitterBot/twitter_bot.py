from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from constants import *


class TwitterBot:
    def __init__(self, driver) -> None:
        self._driver = driver

    def enter_user(self, user: str) -> None:
        username_input = self._driver.find_element(By.XPATH, USERNAME_XPATH)

        username_input.send_keys(user)

    def hit_continue(self) -> None:
        continue_button = self._driver.find_element(By.XPATH, CONTINUE_XPATH)

        continue_button.click()
        sleep(1)

    def hit_login(self) -> None:
        login_button = self._driver.find_element(By.CSS_SELECTOR, LOGIN_SELECTOR)

        login_button.click()
        sleep(1)

    def enter_password(self, password: str) -> None:
        password_input = self._driver.find_element(By.XPATH, PASSWORD_XPATH)

        password_input.send_keys(password)

    def enter_email(self, email: str) -> None:
        email_input = self._driver.find_element(By.NAME, EMAIL_INPUT_NAME)

        email_input.send_keys(email)

    def tweet(self, message: str) -> None:
        twitter_input = self._driver.find_element(By.CSS_SELECTOR, TWEET_INPUT_SELECTOR)
        post_button = self._driver.find_element(By.CSS_SELECTOR, POST_BUTTON_SELECTOR)

        twitter_input.send_keys(message)
        post_button.click()

    def login(self, user: str, password: str, email: str) -> None:
        self._driver.get("https://x.com/login")

        print("Entering username...")
        self.enter_user(user)

        print("User entered, clicking login button")
        self.hit_continue()

        try:
            print("Entering password...")
            self.enter_password(password)

            self.hit_login()
        except NoSuchElementException:
            print("Password failed, trying with capcha verification")

            print("Entering email...")
            self.enter_email(email)
            self.hit_continue()

            print("Email entered, entering login button")
            self.enter_password(password)

            print("Password entered, clicking login button")
            self.hit_login()
