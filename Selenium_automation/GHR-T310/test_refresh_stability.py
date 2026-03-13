import time
import os
import cv2
import pyautogui
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# folders
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

if not os.path.exists("videos"):
    os.makedirs("videos")

# screen size
screen_size = pyautogui.size()

# video setup
fourcc = cv2.VideoWriter_fourcc(*"XVID")
video = cv2.VideoWriter("videos/refresh_test.avi", fourcc, 8.0, screen_size)

print("Starting Refresh Stability Test")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

pages = {
    "homepage": "https://ghorerbazar.com",
    "product_list": "https://ghorerbazar.com/shop",
    "cart": "https://ghorerbazar.com/cart"
}

refresh_count = 3

for page_name, url in pages.items():

    driver.get(url)
    time.sleep(4)

    for i in range(refresh_count):

        print(f"{page_name} refresh {i+1}")

        driver.refresh()
        time.sleep(3)

        screenshot_name = f"screenshots/{page_name}_refresh_{i+1}.png"
        driver.save_screenshot(screenshot_name)

        # capture screen for video
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        video.write(frame)

video.release()

driver.quit()

print("Test Completed")