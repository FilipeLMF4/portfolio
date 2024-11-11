from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

EMAIL = "email"
PASSWORD = "pass"
URL = ("https://www.linkedin.com/jobs/search/?currentJobId=3817328328&f_AL=true&geoId=101165590&"
       "keywords=Python%20developer&"
       "location=United%20Kingdom&"
       "origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&"
       "refresh=true"
       )

# Start driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Login
time.sleep(3)
login_button = driver.find_element(By.CLASS_NAME, value="nav__button-secondary")
login_button.click()

time.sleep(3)
username_input = driver.find_element(By.ID, value="username")
password_input = driver.find_element(By.ID, value="password")

username_input.send_keys(EMAIL)
password_input.send_keys(PASSWORD, Keys.ENTER)

# Close messaging tab
time.sleep(3)
messaging_tab = driver.find_element(By.CLASS_NAME, value="msg-overlay-bubble-header__button")
messaging_tab.click()

# Get all jobs in page
jobs = driver.find_elements(By.CSS_SELECTOR, value=".scaffold-layout__list-container .scaffold-layout__list-item")

for job in jobs:
    div = job.find_element(By.CLASS_NAME, value="job-card-container")
    job_title = div.find_element(By.CLASS_NAME, value="job-card-list__title")
    company_name = div.find_element(By.CLASS_NAME, value="job-card-container__primary-description")
    driver.execute_script("arguments[0].scrollIntoView()", div)
    div.click()
    time.sleep(2)
    save_button = driver.find_element(By.CLASS_NAME, value="jobs-save-button")
    if save_button.find_element(By.CSS_SELECTOR, value="span").text.strip() == "Saved":
        print(f"Job offer for {job_title.text} at {company_name.text} already saved.")
    else:
        save_button.click()
        print(f"Saved job offer for {job_title.text} at {company_name.text}")
    follow_button = driver.find_element(By.CLASS_NAME, value="follow")
    driver.execute_script("arguments[0].scrollIntoView()", follow_button)
    time.sleep(2)
    if "is-following" in follow_button.get_attribute("class"):
        print(f"Already following {company_name.text}.")
    else:
        try:
            follow_button.click()
            print(f"Now following {company_name.text}.")
        except ElementClickInterceptedException:
            print(f"Follow button not clickable for {company_name.text}.")
    print("--------------------------------------------------------------")
    time.sleep(2)

print(f"{len(jobs)} jobs saved. Exiting...")

driver.quit()
