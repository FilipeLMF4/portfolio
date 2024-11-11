from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime

# Keep Chrome brwoser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Install Selenium webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

# For amazon item
# Find by class name
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# # Find by name
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
#
# # Find by ID
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
#
# # Find by CSS Selector
# doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(doc_link.text)
#
# # Find by XPath
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)


# Challenge
times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .menu a")

event_dict = {}
for i in range(len(times)):
    event_dict[i] = {
        "time": times[i].get_attribute("datetime").split("T")[0],
        "name": events[i].text
    }

print(event_dict)

# driver.close()  # Closes a tab
driver.quit()  # Closes the program/driver
