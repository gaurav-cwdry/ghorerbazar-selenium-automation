import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

print("Starting SEO URL Structure Test")

os.makedirs("screenshots", exist_ok=True)
os.makedirs("reports", exist_ok=True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

url = "https://ghorerbazar.com/shop"

driver.get(url)

time.sleep(5)

driver.save_screenshot("screenshots/seo_url_page.png")

current_url = driver.current_url

report = open("reports/seo_url_test_report.txt", "w")

report.write("SEO URL Structure Test\n")
report.write("-----------------------\n")
report.write("URL Tested: " + current_url + "\n")

# simple SEO validation
if "?" not in current_url and "=" not in current_url:

    print("TEST PASSED - URL is SEO friendly")

    report.write("Result: PASS\n")
    report.write("URL structure is readable and SEO friendly\n")

else:

    print("TEST FAILED - URL contains parameters")

    report.write("Result: FAIL\n")
    report.write("URL contains query parameters\n")

driver.save_screenshot("screenshots/seo_result.png")

report.close()

driver.quit()

print("Test Finished")