import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScqpbMdB_INfO7uZ8ZhCMwaz04Ei3I3shonMpi6y_XLwp3cTA/viewform?usp=sf_link"


class Seleniumbot:
    def __init__(self, url):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument("window-size=1920,1080")

        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(url)
        time.sleep(3)

    def find_and_fill(self, address_item, price_item, link_item):
        address_input = self.driver.find_element(
            By.XPATH,
            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
        )

        price_input = self.driver.find_element(
            By.XPATH,
            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
        )

        link_input = self.driver.find_element(
            By.XPATH,
            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
        )

        submit_button = self.driver.find_element(
            By.XPATH,
            value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'
        )

        address_input.send_keys(address_item)
        price_input.send_keys(price_item)
        link_input.send_keys(link_item)
        time.sleep(1)
        submit_button.click()
        time.sleep(2)

    def submit_another(self):
        another_response = self.driver.find_element(
            By.XPATH,
            value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a'
        )

        another_response.click()
        time.sleep(2)


# Web Scraping
response = requests.get(ZILLOW_URL)
soup = BeautifulSoup(response.text, "html.parser")

properties = soup.find_all(name="a", class_="property-card-link")
addresses = soup.find_all(name="address")
prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")

prices_list = [price.text.split("+")[0].split('/')[0] for price in prices]
properties_links = [prop.get("href") for prop in properties]
addresses_list = [address.text.strip().replace(" |", "") for address in addresses]

# Form filling
form_bot = Seleniumbot(FORM_URL)
for item in range(len(prices_list)):
    form_bot.find_and_fill(addresses_list[item], prices_list[item], properties_links[item])
    print(f"Data successfully submitted ({item+1}/{len(prices_list)}).")
    print(f"Address: {addresses_list[item]}")
    print(f"Price per month: {prices_list[item]}")
    print(f"Property link: {properties_links[item]}")
    print("-----------------------------------------")
    if item < len(prices_list) - 1:
        form_bot.submit_another()

form_bot.driver.quit()
print("All data submitted.")
