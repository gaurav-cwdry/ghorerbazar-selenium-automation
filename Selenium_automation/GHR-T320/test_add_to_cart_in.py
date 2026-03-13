import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

print("Starting Add To Cart Test")

os.makedirs("screenshots", exist_ok=True)
os.makedirs("reports", exist_ok=True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

wait = WebDriverWait(driver, 20)

report = open("reports/add_to_cart_report.txt", "w")

try:

    # Step 1: open shop page
    driver.get("https://ghorerbazar.com/shop")

    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ul.products"))
    )

    driver.save_screenshot("screenshots/shop_page.png")

    print("Shop page opened")

    # Step 2: click first product
    product = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "ul.products li.product a"))
    )

    product.click()

    print("Product page opened")

    wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    driver.save_screenshot("screenshots/product_page.png")

    # Step 3: click add to cart button
    add_to_cart = wait.until(
        EC.element_to_be_clickable((By.NAME, "add-to-cart"))
    )

    add_to_cart.click()

    print("Add to cart button clicked")

    # Step 4: verify cart message
    success_message = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".woocommerce-message"))
    )

    driver.save_screenshot("screenshots/add_to_cart_success.png")

    if success_message:

        print("TEST PASSED - Product added to cart")

        report.write("Result: PASS\n")
        report.write("Product successfully added to cart\n")

    else:

        print("TEST FAILED - Add to cart message not found")

        report.write("Result: FAIL\n")

except Exception as e:

    print("TEST FAILED")
    print(e)

    report.write("Result: FAIL\n")
    report.write("Error: " + str(e))

driver.quit()

report.close()

print("Test Finished")