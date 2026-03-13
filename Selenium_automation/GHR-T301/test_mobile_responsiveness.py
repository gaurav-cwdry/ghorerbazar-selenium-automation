import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

print("Starting Mobile Responsiveness Test")

os.makedirs("screenshots", exist_ok=True)
os.makedirs("reports", exist_ok=True)

options = webdriver.ChromeOptions()

# mobile screen simulation
options.add_argument("--window-size=375,812")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

url = "https://ghorerbazar.com/shop"

driver.get(url)

time.sleep(6)

driver.save_screenshot("screenshots/mobile_view_page.png")

report = open("reports/mobile_responsive_test_report.txt", "w")

report.write("Mobile Responsiveness Test\n")
report.write("---------------------------\n")
report.write("URL: https://ghorerbazar.com/shop\n")
report.write("Viewport: 375x812\n")

try:

    # WooCommerce product selector
    products = driver.find_elements(By.CSS_SELECTOR, "li.product")

    product_count = len(products)

    print("Product cards detected:", product_count)

    report.write("Product cards found: " + str(product_count) + "\n")

    # check horizontal scroll
    scroll_width = driver.execute_script("return document.body.scrollWidth")
    client_width = driver.execute_script("return document.body.clientWidth")

    report.write("Scroll Width: " + str(scroll_width) + "\n")
    report.write("Client Width: " + str(client_width) + "\n")

    if product_count > 0 and scroll_width <= client_width:

        print("TEST PASSED - Mobile layout responsive")

        report.write("Result: PASS\n")
        report.write("Layout adapts correctly to mobile screen\n")

    else:

        print("TEST FAILED - Layout issue detected")

        report.write("Result: FAIL\n")
        report.write("Layout may not be responsive or product cards not detected\n")

except Exception as e:

    print("TEST FAILED")

    report.write("Result: FAIL\n")
    report.write("Error: " + str(e) + "\n")

driver.save_screenshot("screenshots/mobile_test_result.png")

report.close()

driver.quit()

print("Test Finished")