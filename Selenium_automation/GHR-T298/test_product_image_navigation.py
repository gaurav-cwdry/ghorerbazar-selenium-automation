import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

print("Starting Product Image Navigation Test")

# folders
os.makedirs("screenshots", exist_ok=True)
os.makedirs("reports", exist_ok=True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

url = "https://ghorerbazar.com/shop"

driver.get(url)

time.sleep(5)

driver.save_screenshot("screenshots/product_listing_page.png")

report = open("reports/product_image_navigation_report.txt", "w")

report.write("Product Image Navigation Test\n")
report.write("---------------------------------\n")
report.write("URL Tested: https://ghorerbazar.com/shop\n")

try:

    # find product images
    images = driver.find_elements(By.CSS_SELECTOR, "img")

    if len(images) == 0:

        print("TEST FAILED - No product images found")

        report.write("Result: FAIL\n")
        report.write("Reason: No product images detected\n")

    else:

        first_image = images[0]

        print("Clicking first product image")

        driver.execute_script("arguments[0].scrollIntoView();", first_image)

        time.sleep(2)

        first_image.click()

        time.sleep(5)

        driver.save_screenshot("screenshots/product_detail_page.png")

        current_url = driver.current_url

        if current_url != url:

            print("TEST PASSED - Product page opened")

            report.write("Result: PASS\n")
            report.write("Product page opened successfully\n")
            report.write("New URL: " + current_url + "\n")

        else:

            print("TEST FAILED - Navigation did not occur")

            report.write("Result: FAIL\n")
            report.write("Product page did not open\n")

except Exception as e:

    print("TEST FAILED")

    report.write("Result: FAIL\n")
    report.write("Error: " + str(e) + "\n")

driver.save_screenshot("screenshots/final_state.png")

report.close()

driver.quit()

print("Test Finished")
