import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

print("Starting Product Card Display Test")

# create folders
os.makedirs("screenshots", exist_ok=True)
os.makedirs("reports", exist_ok=True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

url = "https://ghorerbazar.com/shop"

driver.get(url)

time.sleep(5)

driver.save_screenshot("screenshots/product_listing_page.png")

# find product cards
products = driver.find_elements(By.CSS_SELECTOR, ".product-item")

product_count = len(products)

print("Total Product Cards Found:", product_count)

# report file
report = open("reports/product_card_test_report.txt", "w")

report.write("Product Card Display Test Report\n")
report.write("--------------------------------\n")
report.write("URL: https://ghorerbazar.com/shop\n")
report.write("Total Product Cards Found: " + str(product_count) + "\n")

if product_count > 0:

    print("TEST PASSED - Product cards are visible")

    report.write("Result: PASS\n")

else:

    print("TEST FAILED - No product cards found")

    report.write("Result: FAIL\n")

driver.save_screenshot("screenshots/product_card_result.png")

report.close()

driver.quit()

print("Test Finished")