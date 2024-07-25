from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://secure-retreat-92358.herokuapp.com/'

driver = webdriver.Chrome()

driver.get(URL)

first_name_input = driver.find_element(By.NAME, "fName")
last_name_input = driver.find_element(By.NAME, "lName")
email_name_input = driver.find_element(By.NAME, "email")
submit_button = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")

first_name_input.send_keys("Leo")
last_name_input.send_keys("last name")
email_name_input.send_keys("mail@mail.com")

submit_button.click()
