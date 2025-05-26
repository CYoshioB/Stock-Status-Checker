from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url_list = [
    "https://gundamplacestore.com/collections/real-grade/products/1-144-rg-gundam-astray-red-frame",    #0
    "https://gundamplacestore.com/collections/real-grade/products/rg-32-rx-93-nu-gundam",               #1
    "https://usagundamstore.com/collections/rg/products/rg-1-144-16-msm-07s-zgok-chars-custom",         #2
    "https://usagundamstore.com/collections/rg/products/rg-1-144-32-rx-93-nu-gundam",                   #3
    "https://gundamplanet.com/collections/gundam-9/products/rg-msn-02-zeong",                           #4
    "https://gundamplanet.com/collections/gundam-9/products/rg-rx-93-nu-gundam",                        #5
    "https://newtype.us/p/U1QAHfKuXlryFcimMpSJ/h/rg-36-rx-93-hi-nu-gundam",                             #6
    "https://newtype.us/p/ORUrU23xYDLWOgNOm3R1/h/rg-37-god-gundam"                                      #7
]
page_url = url_list[4]
debug = False

service = Service()
options = Options()

options.add_argument('-headless')
options.add_argument('-no-sandbox')
options.add_argument('-disable-dev-shm-usage')


driver = webdriver.Firefox(service=service, options=options)
wait_time = 3

try:
    driver.get(page_url)

    storeName_elem = driver.find_element(By.XPATH, "//meta[@property='og:site_name']")
    productName_elem = driver.find_element(By.XPATH, "//meta[@property='og:title']")
    siteName_elem = driver.find_element(By.XPATH, "//meta[@property='og:url']")

except Exception as e:
    print("HTML element not found!")

else:
    storeName = storeName_elem.get_attribute("content")
    productName = productName_elem.get_attribute("content")
    siteName = siteName_elem.get_attribute("content")

    print("Checking for stock at:")
    print(storeName)
    print(productName)

    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    time.sleep(wait_time)
    driver.set_window_size(1920, 1500)

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