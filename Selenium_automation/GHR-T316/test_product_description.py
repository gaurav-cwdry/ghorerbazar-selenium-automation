import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

print("Starting Product Description Test")

os.makedirs("screenshots", exist_ok=True)
os.makedirs("reports", exist_ok=True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

wait = WebDriverWait(driver, 20)

report = open("reports/product_description_report.txt", "w")

try:

    # Step 1: open shop page
    driver.get("https://ghorerbazar.com/shop")

    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ul.products"))
    )

    driver.save_screenshot("screenshots/product_listing_page.png")

    print("Listing page loaded")

    # Step 2: click first product
    product = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "ul.products li.product a"))
    )

    driver.execute_script("arguments[0].scrollIntoView();", product)
    product.click()

    print("Product clicked")

    # Step 3: wait for product page
    wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    driver.save_screenshot("screenshots/product_page.png")

    # Step 4: check description tab
    description_tab = driver.find_elements(By.ID, "tab-description")

    if len(description_tab) > 0:

        print("TEST PASSED - Description section exists")

        report.write("Result: PASS\n")
        report.write("Description section found\n")

    else:

        print("TEST FAILED - Description section missing")

        report.write("Result: FAIL\n")
        report.write("Description section not found\n")

    driver.save_screenshot("screenshots/description_section.png")

except Exception as e:

    print("TEST FAILED")
    print(e)

    report.write("Result: FAIL\n")
    report.write("Error: " + str(e))

driver.quit()

report.close()

print("Test Finished")