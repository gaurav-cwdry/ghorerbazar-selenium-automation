import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

print("Starting Product Hover Effect Test")

os.makedirs("screenshots", exist_ok=True)
os.makedirs("reports", exist_ok=True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

url = "https://ghorerbazar.com/shop"

driver.get(url)

time.sleep(5)

driver.save_screenshot("screenshots/product_page.png")

# find product cards
products = driver.find_elements(By.CSS_SELECTOR, ".product-item")

report = open("reports/hover_test_report.txt", "w")

report.write("Product Hover Effect Test\n")
report.write("-------------------------\n")

if len(products) > 0:

    first_product = products[0]

    actions = ActionChains(driver)

    actions.move_to_element(first_product).perform()

    print("Hover action performed")

    time.sleep(3)

    driver.save_screenshot("screenshots/hover_effect.png")

    report.write("Result: PASS\n")
    report.write("Hover effect triggered on product card\n")

else:

    print("TEST FAILED - No product cards found")

    report.write("Result: FAIL\n")
    report.write("No product cards detected\n")

report.close()

driver.quit()

print("Test Finished")