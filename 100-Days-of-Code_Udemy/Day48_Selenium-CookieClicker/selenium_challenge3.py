from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Filipe")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Ferreira")

email = driver.find_element(By.NAME, value="email")
email.send_keys("email")

button = driver.find_element(By.CLASS_NAME, value="btn")
button.click()

# driver.quit()