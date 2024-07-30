from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


from constants import *
from time import sleep


class InstaBot:
    """Bot that controls the instagram interaction through selenium"""

    def __init__(self, browser: Chrome) -> None:
        self._browser = browser

    def go_to(self, url: str) -> None:
        """Visits the target page"""
        self._browser.get(url)

    def fill_user(self, user: str) -> None:
        """Enters a username in the login"""
        user_input = self._browser.find_element(By.NAME, USERNAME_INPUT_NAME)

        user_input.send_keys(user)

    def fill_password(self, password: str) -> None:
        """Enters a password in the login"""
        password_input = self._browser.find_element(By.NAME, PASSWORD_INPUT_NAME)

        password_input.send_keys(password)

    def click_login(self):
        """clicks the login button"""
        login_button = self._browser.find_element(
            By.CSS_SELECTOR, LOGIN_BUTTON_SELECTOR
        )

        login_button.click()

    def dissmiss_popup(self) -> None:
        """Dismiss the notifications pop up"""
        not_now_button = self._browser.find_element(DISMISS_NOTIFICATIONS)

        not_now_button.click()

    def login(self, user: str, password: str) -> None:
        """Receives username and password to log to instagram"""
        self.fill_user(user)
        self.fill_password(password)

        self.click_login()

    def follow_followers(self):
        """Follows all the followers to an account"""

        followers_link = self._browser.find_element(By.CSS_SELECTOR, FOLLOWERS_SELECTOR)

        followers_link.click()

        sleep(10)

        follow_buttons = self._browser.find_elements(By.XPATH, FOLLOW_BUTTONS)

        print(f"fount {len(follow_buttons)} accounts to follow")

        for follow_button in follow_buttons:
            follow_button.click()
