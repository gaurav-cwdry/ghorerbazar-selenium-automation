import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

print("Starting Listing Page Load Speed Test")

# screenshot folder create
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

start_time = time.time()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# listing page open
driver.get("https://ghorerbazar.com/shop")

end_time = time.time()

load_time = round(end_time - start_time, 2)

print("Page Load Time:", load_time, "seconds")

# screenshot save
driver.save_screenshot("screenshots/listing_page_loaded.png")

# report save
report = open("screenshots/load_speed_report.txt", "w")
report.write("Listing Page Load Speed Test\n")
report.write("URL: https://ghorerbazar.com/shop\n")
report.write("Load Time: " + str(load_time) + " seconds\n")

if load_time < 3:
    print("TEST PASSED - Page loaded within acceptable time")
    report.write("Result: PASS\n")
else:
    print("TEST FAILED - Page load too slow")
    report.write("Result: FAIL\n")

report.close()

time.sleep(3)

driver.quit()