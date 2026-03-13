import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

print("Starting Broken Image Test")

# folders create
os.makedirs("screenshots", exist_ok=True)
os.makedirs("reports", exist_ok=True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

url = "https://ghorerbazar.com/shop"
driver.get(url)

time.sleep(5)

driver.save_screenshot("screenshots/product_listing_page.png")

images = driver.find_elements(By.TAG_NAME, "img")

broken_images = []

for img in images:

    src = img.get_attribute("src")

    if src:

        try:
            response = requests.get(src)

            if response.status_code != 200:

                broken_images.append(src)

        except:
            broken_images.append(src)

# report file
report_file = open("reports/broken_image_report.txt", "w")

report_file.write("Broken Image Test Report\n")
report_file.write("------------------------\n")
report_file.write("URL: https://ghorerbazar.com/shop\n")
report_file.write("Total Images Found: " + str(len(images)) + "\n")

if len(broken_images) == 0:

    print("TEST PASSED - No broken images found")

    report_file.write("Result: PASS\n")
    report_file.write("Broken Images: None\n")

else:

    print("TEST FAILED - Broken images detected")

    report_file.write("Result: FAIL\n")
    report_file.write("Broken Images:\n")

    for img in broken_images:
        report_file.write(img + "\n")

driver.save_screenshot("screenshots/image_test_result.png")

report_file.close()

driver.quit()

print("Test Finished")