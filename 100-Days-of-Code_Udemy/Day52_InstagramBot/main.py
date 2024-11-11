from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

USERNAME = "user"
PASSWORD = "password"
TARGET_ACCOUNT = "taylorswift"
NR_FOLLOWERS_REFRESH = 3


class InstaFollower:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument("window-size=1920,1080")

        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.url = "https://www.instagram.com"

    def login(self, user, password):
        self.driver.get(f"{self.url}/accounts/login/")
        time.sleep(3)
        login_cookies = self.driver.find_element(
            By.XPATH,
            value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]'
        )
        login_cookies.click()

        time.sleep(2)
        username_field = self.driver.find_element(
            By.XPATH,
            value='//*[@id="loginForm"]/div/div[1]/div/label/input'
        )
        password_field = self.driver.find_element(
            By.XPATH,
            value='//*[@id="loginForm"]/div/div[2]/div/label/input'
        )

        username_field.send_keys(user)
        password_field.send_keys(password, Keys.ENTER)

        time.sleep(5)
        decline_save = self.driver.find_element(
            By.XPATH,
            value='//div[contains(text(), "Agora não")]'
        )
        decline_save.click()

        time.sleep(2)
        decline_notifications = self.driver.find_element(
            By.XPATH,
            value='//button[contains(text(), "Agora Não")]'
        )
        decline_notifications.click()
        time.sleep(2)

    def find_followers(self, target_account):
        self.driver.get(f"{self.url}/{target_account}")

        time.sleep(5)
        followers = self.driver.find_element(
            By.XPATH,
            value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a'
        )
        followers.click()
        time.sleep(5)

    def follow(self):
        follow_buttons = self.driver.find_elements(
            By.XPATH,
            value="//div[contains(text(), 'Seguir')]"
        )
        for button in follow_buttons:
            self.driver.execute_script("arguments[0].scrollIntoView()", button)
            try:
                time.sleep(1)
                button.click()
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancelar')]")
                cancel_button.click()
            finally:
                time.sleep(1)

        return len(follow_buttons)


bot = InstaFollower()
bot.login(USERNAME, PASSWORD)
bot.find_followers(TARGET_ACCOUNT)
total_follows = 0
for _ in range(NR_FOLLOWERS_REFRESH):
    follows = bot.follow()
    total_follows += follows
    time.sleep(2)

bot.driver.quit()
print("Bot finished successfully.")
print(f"Followed {total_follows} total accounts.")
