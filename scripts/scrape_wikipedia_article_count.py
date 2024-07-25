from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://en.wikipedia.org/wiki/Main_Page'

driver = webdriver.Chrome()

driver.get(URL)

article_count = driver.find_element(By.CSS_SELECTOR, "a[title='Special:Statistics']")

print(article_count.text)
