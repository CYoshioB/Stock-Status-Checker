from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service()
options = Options()

options.add_argument('-headless')
options.add_argument('-no-sandbox')
options.add_argument('-disable-dev-shm-usage')


driver = webdriver.Firefox(service=service, options=options)
wait_time = 2

page_url = input("Please provide a url to check: ")

try:
    driver.get(page_url)

except Exception as e:
    print("HTML element not found!")

else:
    productName = driver.find_element(By.XPATH, "//meta[@property='og:title']").get_attribute("content")
    siteName = driver.find_element(By.XPATH, "//meta[@property='og:url']").get_attribute("content")
    if "newtype" in page_url:
        storeName = "Newtype"
    else:
        storeName = driver.find_element(By.XPATH, "//meta[@property='og:site_name']").get_attribute("content")

    print("Checking for stock of:")
    print(storeName)
    print(productName)

    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    time.sleep(wait_time)

    page_source = driver.page_source
    add_to_count = page_source.lower().count("add to ")
    in_stock_count = page_source.lower().count("in stock")

    if add_to_count > 5 or in_stock_count > 2:
        print("\nGundam kit is now in stock!")
        print("Get it here:", siteName)
    else:
        print("\nGundam kit is not in stock...")

finally:
    driver.quit()