from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

nr_articles = driver.find_element(By.ID, value="articlecount").text.split(" ")[0]

print(f"Current Wikipedia total number of articles: {nr_articles}")


# # Click on links
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Fill form and click
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)

# driver.quit()
