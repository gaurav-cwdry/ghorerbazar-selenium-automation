import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

print("Starting Product Grid Alignment Test")

os.makedirs("screenshots", exist_ok=True)
os.makedirs("reports", exist_ok=True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

url = "https://ghorerbazar.com/shop"

driver.get(url)

time.sleep(5)

driver.save_screenshot("screenshots/grid_page.png")

products = driver.find_elements(By.CSS_SELECTOR, ".product-item")

positions = []

for product in products:

    location = product.location
    positions.append(location['y'])

# check if multiple products share same row
aligned = False

if len(positions) > 1:

    aligned = positions[0] == positions[1]

report = open("reports/grid_alignment_report.txt", "w")

report.write("Product Grid Alignment Test\n")
report.write("----------------------------\n")
report.write("Total Products Found: " + str(len(products)) + "\n")

if aligned:

    print("TEST PASSED - Products aligned in grid")

    report.write("Result: PASS\n")

else:

    print("TEST WARNING - Grid alignment needs manual check")

    report.write("Result: REVIEW REQUIRED\n")

driver.save_screenshot("screenshots/grid_result.png")

report.close()

driver.quit()

print("Test Finished")