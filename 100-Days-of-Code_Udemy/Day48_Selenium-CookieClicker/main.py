from selenium import webdriver
from selenium.webdriver.common.by import By
import time

BUY_AVAIL = True
TIME_CHECK_DIFF = 7

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")
store = driver.find_element(By.ID, value="store")

time_start = time.time()
time_end = time_start + 5*60

while time.time() <= time_end:
    cookie.click()
    if time.time() >= time_start + TIME_CHECK_DIFF:
        upgrades = store.find_elements(By.XPATH, "*")
        upgrades.pop()
        for upgrade in upgrades[::-1]:
            if upgrade.get_attribute("class") == "grayed":
                continue
            upgrade.click()
            break

        time_start = time.time()

cookies_per_second = driver.find_element(By.ID, value="cps")
print(cookies_per_second.text)

driver.quit()

# High scores
# 1 sec, buy most expensive = 64.2
# 2 sec, buy most expensive = 60.2
# 3 sec, buy most expensive = 69
# 4 sec, buy most expensive = 82.6
# 5 sec, buy most expensive = 109.6
# 6 sec, buy most expensive = 115.2
# 7 sec, buy most expensive = 137.4
# 8 sec, buy most expensive = 130.4
# 9 sec, buy most expensive = 130.8
# 10 sec, buy most expensive = 74
