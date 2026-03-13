from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

print("Starting Selenium Test...")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# screenshot folder
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

# open website
driver.get("https://ghorerbazar.com/")
time.sleep(5)

print("Website opened")

driver.save_screenshot("screenshots/homepage_loaded.png")

try:

    # find product images
    products = driver.find_elements(By.CSS_SELECTOR, "img")

    print("Total images found:", len(products))

    product = products[5]

    # scroll to product
    driver.execute_script("arguments[0].scrollIntoView();", product)
    time.sleep(2)

    # click using javascript (more reliable)
    driver.execute_script("arguments[0].click();", product)

    print("Product clicked")

    time.sleep(5)

    driver.save_screenshot("screenshots/product_details_page.png")

    print("TEST PASSED - Product page opened")

except Exception as e:

    print("TEST FAILED")
    print("Error:", e)

    driver.save_screenshot("screenshots/error.png")

time.sleep(3)

driver.quit()

print("Test finished")