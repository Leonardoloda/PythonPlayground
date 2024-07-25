from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://www.python.org/'

driver = webdriver.Chrome()

driver.get(URL)

events = []

title = driver.find_element(By.CSS_SELECTOR, ".event-widget .widget-title")
dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul.menu li time")
events = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul.menu li a")

for i in range(len(events)):
    date = dates[i].text
    name = events[i].text

    events.append({
        'date': date,
        'name': name
    })
