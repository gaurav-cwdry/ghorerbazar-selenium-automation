from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

print("TEST STARTED : Verify Homepage Responsiveness (Tablet)")

# Open browser
driver = webdriver.Chrome()

# Tablet viewport size (iPad)
driver.set_window_size(768, 1024)
print("Tablet viewport set (768x1024)")

# Open website
driver.get("https://ghorerbazar.com/")
print("Website opened")

time.sleep(3)

# Step 1: Check Logo
try:
    logo = driver.find_element(By.CLASS_NAME,"logo")
    print("STEP 1 PASS : Logo visible")
except:
    print("STEP 1 FAIL : Logo not visible")

# Step 2: Check Search box
try:
    search = driver.find_element(By.NAME,"q")
    print("STEP 2 PASS : Search box visible")
except:
    print("STEP 2 FAIL : Search box missing")

# Step 3: Check Banner
try:
    banner = driver.find_element(By.CLASS_NAME,"swiper-slide")
    print("STEP 3 PASS : Banner visible")
except:
    print("STEP 3 FAIL : Banner missing")

# Step 4: Scroll page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
print("STEP 4 : Page scrolled")

time.sleep(2)

# Take screenshot for report
driver.save_screenshot("tablet_homepage_test.png")
print("Screenshot saved for report")

# Close browser
driver.quit()

print("TEST FINISHED")