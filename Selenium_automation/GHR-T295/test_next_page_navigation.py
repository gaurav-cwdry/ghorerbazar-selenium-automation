import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

print("Starting Next Page Navigation Test")

os.makedirs("screenshots", exist_ok=True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://ghorerbazar.com/shop")

time.sleep(5)

driver.save_screenshot("screenshots/page1.png")

print("Page 1 loaded")

try:

    # scroll to bottom where pagination exists
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    # find pagination buttons
    pagination_links = driver.find_elements(By.CSS_SELECTOR, "a")

    next_clicked = False

    for link in pagination_links:

        text = link.text.strip()

        if text == "2" or "Next" in text or ">" in text:

            driver.execute_script("arguments[0].click();", link)
            next_clicked = True
            break

    if next_clicked:

        time.sleep(5)

        driver.save_screenshot("screenshots/page2.png")

        print("TEST PASSED - Next page opened successfully")

    else:

        print("TEST FAILED - Pagination button not found")

except Exception as e:

    print("TEST FAILED")
    print(e)

driver.quit()

print("Test Finished")