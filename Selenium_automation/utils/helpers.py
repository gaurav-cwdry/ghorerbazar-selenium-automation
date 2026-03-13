import os
from datetime import datetime


def save_screenshot(driver, test_name, label):
    os.makedirs("screenshots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = f"screenshots/{test_name}_{label}_{timestamp}.png"
    driver.save_screenshot(path)
    return path