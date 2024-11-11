from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from datetime import datetime

EMAIL = "email"
PASSWORD = "password"
BASE_URL = "https://pt.linkedin.com/"
JOB_URL = ["https://www.linkedin.com/jobs/search/?"
           "currentJobId=4045744452&"
           "distance=10&"
           "geoId=102520832&"
           "keywords=Mechanical%20Engineer&"
           "origin=JOB_SEARCH_PAGE_JOB_FILTER&"
           "refresh=true"]

# Start driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)
driver.get(BASE_URL)
time.sleep(5)

# Reject cookies
cookies_button = driver.find_element(By.XPATH, value="/html/body/div[1]/div/section/div/div[2]/button[2]")
cookies_button.click()
time.sleep(2)

# Login
login_button = driver.find_element(By.CLASS_NAME, value="nav__button-secondary")
login_button.click()
time.sleep(3)

username_input = driver.find_element(By.ID, value="username")
password_input = driver.find_element(By.ID, value="password")

username_input.send_keys(EMAIL)
password_input.send_keys(PASSWORD, Keys.ENTER)

# Check for verification code
time.sleep(3)
try:
    verification = driver.find_element(By.ID, value="input__email_verification_pin")
except NoSuchElementException:
    pass
else:
    verification_code = str(input("Please check for verification code: \n"))
    verification.send_keys(verification_code, Keys.ENTER)

# Close tabs
time.sleep(3)
try:
    terms_tab = driver.find_element(By.XPATH, value="/html/body/div[6]/div/section/button")
except NoSuchElementException:
    pass
else:
    terms_tab.click()
    time.sleep(1)

messaging_tab = driver.find_element(By.XPATH, value="//*[@id='msg-overlay']/div[1]/header/div[3]/button")
messaging_tab.click()

# Go to job search
count = 0
loc = 1
logs = []
for url in JOB_URL:
    driver.get(url)
    time.sleep(3)

    # Get all jobs in page
    logs.append(f"Results for search at location {loc}")
    next_page = 1

    next_job_page = True
    while next_job_page:
        jobs = driver.find_elements(By.CSS_SELECTOR, value=".scaffold-layout__list-container .scaffold-layout__list-item")
        for job in jobs:
            div = job.find_element(By.CLASS_NAME, value="job-card-container")
            job_title = div.find_element(By.CLASS_NAME, value="job-card-list__title")
            company_name = div.find_element(By.CLASS_NAME, value="job-card-container__primary-description")
            driver.execute_script("arguments[0].scrollIntoView()", div)
            element_class_names = div.get_attribute("class").split(" ")
            div.click()

            time.sleep(2)
            if "job-card-list--is-dismissed" in element_class_names:
                message = f"Job offer {job_title.text} at {company_name.text} dismissed previously."
            else:
                job_info = driver.find_element(By.ID, value="job-details")
                body = job_info.find_element(By.XPATH, value='//*[@id="job-details"]/div/p')
                dismiss_button = div.find_element(By.CLASS_NAME, value="job-card-container__action")

                if "Nederlands" in body.text:
                    dismiss_button.click()
                    message = f"Job offer {job_title.text} at {company_name.text} dismissed (Dutch is required)."
                else:
                    try:
                        save_button = driver.find_element(By.CLASS_NAME, value="jobs-save-button")
                    except NoSuchElementException:
                        message = f"Already applied for {job_title.text} at {company_name.text}"
                    else:
                        if save_button.find_element(By.CSS_SELECTOR, value="span").text.strip() == "Saved":
                            message = f"Job offer for {job_title.text} at {company_name.text} already saved."
                        else:
                            save_button.click()
                            count += 1
                            message = f"Saved job offer for {job_title.text} at {company_name.text}"
                            dismiss_button.click()

            print(message)
            print("--------------------------------------------------------------")
            logs.append(message)
            time.sleep(2)

        next_page += 1
        try:
            pages = driver.find_element(By.CLASS_NAME, value="jobs-search-results-list__pagination")
        except NoSuchElementException:
            print("Reached end of pages.")
            next_job_page = False
        else:
            try:
                next_page_button = pages.find_element(By.CSS_SELECTOR, value=f"[aria-label='Page {str(next_page)}']")
            except NoSuchElementException:
                print("Reached end of pages.")
                next_job_page = False
            else:
                next_page_button.click()
                time.sleep(3)

    loc += 1
    logs.append("\n")


print(f"{count} jobs saved. Exiting...")

# driver.quit()

# Write logs to file
today = datetime.now().strftime("%y%m%d_%H%M")
file_name = f"{today}_logs.txt"
with open(file_name, "w") as f:
    for line in logs:
        f.write(f"{line}\n")
        f.write("------------------------------------------------------------------------\n")
