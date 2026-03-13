from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
import os

print("Starting Test...")

driver = webdriver.Chrome()
driver.get("https://ghorerbazar.com/")
driver.maximize_window()

time.sleep(5)

print("Website opened")

# screenshot folder create
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

driver.save_screenshot("screenshots/homepage.png")

images = driver.find_elements(By.TAG_NAME, "img")

print("Total images found:", len(images))

broken_images = 0

for index, img in enumerate(images):

    src = img.get_attribute("src")

    if src:

        response = requests.get(src)

        if response.status_code != 200:
            print("Broken image:", src)
            broken_images += 1

            driver.save_screenshot(f"screenshots/broken_image_{index}.png")

print("Broken Images:", broken_images)

if broken_images == 0:
    print("TEST PASSED - No broken images found")
else:
    print("TEST FAILED - Broken images detected")

time.sleep(3)

driver.quit()