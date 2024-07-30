from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from constants import *
from property import Property


class GoogleBot:
    def __init__(self, url: str) -> None:
        chrome_options = webdriver.ChromeOptions()

        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_experimental_option("detach", True)

        self.chrome = webdriver.Chrome(options=chrome_options)
        self.chrome.implicitly_wait(3)
        self.url = url

    def load_page(self):
        self.chrome.get(self.url)

        sleep(2)

    def close_page(self):
        self.chrome.close()

    def fill_form(self, property: Property):
        inputs = self.chrome.find_elements(By.CSS_SELECTOR, INPUTS_SELECTOR)
        submit_button = self.chrome.find_element(By.CSS_SELECTOR, SUBMIT_SELECTOR)

        address_input = inputs[ADDRESS_INPUT_INDEX]
        price_input = inputs[PRICE_INPUT_INDEX]
        link_input = inputs[LINK_INPUT_INDEX]

        address_input.send_keys(property.address)
        price_input.send_keys(property.price)
        link_input.send_keys(property.url)

        submit_button.click()
