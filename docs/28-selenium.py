from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# You can use selenium to start any browser

chrome_options = webdriver.ChromeOptions()
# to keep it from closing you must enable this option
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# Now you can tell it  to open any website
driver.get(
    "https://www.amazon.com/dp/B0CQYRDB5W/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B0CQYRDB5W&pd_rd_w=VftrR&content-id=amzn1.sym.386c274b-4bfe-4421-9052-a1a56db557ab&pf_rd_p=386c274b-4bfe-4421-9052-a1a56db557ab&pf_rd_r=CW58ZDSD7P1EVAKE4VCJ&pd_rd_wg=W4MUb&pd_rd_r=b6766b85-79ee-410b-81d0-94d0c83615ec&s=furniture&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM")

try:
    # You can use locator to find any element, you pass what's the criteria
    price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
    price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")

    print(f"The price is {price_dollar.text}.{price_cents.text}")
except WebDriverException as e:
    print("Captcha page")

# You can also find by name, really useful for inputs
# product_search = driver.find_element(By.NAME, "field-keywords")

# Or you can just close the tab
# driver.close()

driver.get("https://www.python.org/")

# You can also query by name
search_bar = driver.find_element(By.NAME, "q")
# You can also interact with it by using click
search_bar.click()
# or send a text
search_bar.send_keys("python")
# You can import keys to send special keys
search_bar.send_keys(Keys.RETURN)

# Or query by id
# go_button = driver.find_element(By.ID, "submit")
# go_button.click()

# or by css selectors
first_result = driver.find_element(By.CSS_SELECTOR, ".list-recent-events.menu a")
print("First result is {}".format(first_result.text))

# You can copy the xpath from the browser
submit_bug = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(f"Submit bug is {submit_bug.text}")

# but if you wanna cllose all tabs, you'll need to quite
driver.quit()
