from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os

print("Starting Sale Price Test...")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

driver.get("https://ghorerbazar.com/")
time.sleep(5)

driver.save_screenshot("screenshots/homepage.png")

try:

    prices = driver.find_elements(By.CSS_SELECTOR, "span")

    sale_found = False

    for price in prices:

        text = price.text

        if "৳" in text:

            print("Price detected:", text)

            sale_found = True

    if sale_found:

        print("TEST PASSED - Sale price displayed")

        driver.save_screenshot("screenshots/sale_price.png")

    else:

        print("TEST FAILED - No sale price detected")

except Exception as e:

    print("TEST FAILED")
    print(e)

    driver.save_screenshot("screenshots/error.png")

time.sleep(3)

driver.quit()