from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

import time

FACEBOOK_EMAIL = "email"
FACEBOOK_PASSWORD = "password"
URL = "https://tinder.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

time.sleep(2)
login_button = driver.find_element(
    By.XPATH,
    '//*[@id="c1606223767"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a'
)
login_button.click()

time.sleep(1)
facebook_button = driver.find_element(
    By.XPATH,
    '//*[@id="c1827564203"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button'
)
facebook_button.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(f"Switching to {driver.title}")

time.sleep(2)
cookies_decline = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[4]/button[1]')
cookies_decline.click()
time.sleep(1)

facebook_login_email = driver.find_element(By.ID, "email")
facebook_login_password = driver.find_element(By.ID, "pass")
facebook_login_email.send_keys(FACEBOOK_EMAIL)
facebook_login_password.send_keys(FACEBOOK_PASSWORD, Keys.ENTER)
time.sleep(10)

# Tinder
driver.switch_to.window(base_window)
print(f"Switching to {driver.title}")
allow_loc_button = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[1]/div/div/div[3]/button[1]')
allow_loc_button.click()

time.sleep(2)
decline_notify_button = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[1]/div/div/div[3]/button[2]')
decline_notify_button.click()

time.sleep(2)
cookies_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button')
cookies_button.click()
time.sleep(5)

count = 0
div = '3'
while count < 100:
    time.sleep(2)
    if count > 0:
        div = '4'
    swipe_left = driver.find_element(
        By.XPATH,
        f'/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[{div}]/div/div[2]/button'
    )
    try:
        swipe_left.click()
        count += 1
    except NoSuchElementException:
        time.sleep(2)
    except ElementClickInterceptedException:
        time.sleep(2)
        try:
            decline_tinder_button = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/button[2]')
            decline_tinder_button.click()
        except NoSuchElementException:
            pass

driver.quit()
