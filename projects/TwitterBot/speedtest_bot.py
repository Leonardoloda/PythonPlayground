from time import sleep

from selenium.webdriver.chromium import webdriver
from selenium.webdriver.common.by import By

from constants import *


class SpeedBot:

    def __init__(self, driver: webdriver) -> None:
        self._driver = driver

    def test_speed(self) -> float:
        self._driver.get("https://www.speedtest.net/")

        go_button = self._driver.find_element(By.CSS_SELECTOR, GO_CSS_SELECTOR)

        go_button.click()

        sleep(SPEED_TEST_TIMEOUT)

        internet_result = self._driver.find_element(By.CSS_SELECTOR, SPEED_CSS_SELECTOR)

        return float(internet_result.text)
