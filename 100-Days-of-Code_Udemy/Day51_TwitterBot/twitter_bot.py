from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument("window-size=1920,1080")

        self.driver = webdriver.Chrome(options=self.chrome_options)

        self.twitter_username = "username"
        self.twitter_password = "password"
        self.up = 200
        self.down = 500

    def get_internet_speed(self):
        speedtest_url = "https://www.speedtest.net"
        self.driver.get(speedtest_url)
        time.sleep(3)
        try:
            cookies_button = self.driver.find_element(By.ID, value="onetrust-reject-all-handler")
            cookies_button.click()
        except NoSuchElementException:
            pass

        go_button = self.driver.find_element(By.XPATH,
                                             value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'
                                             )
        go_button.click()

        time.sleep(50)
        down_speed = self.driver.find_element(
            By.XPATH,
            value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'
        )

        up_speed = self.driver.find_element(
            By.XPATH,
            value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
        )

        time.sleep(1)
        print(f'Down: {down_speed.text}')
        print(f'Up: {up_speed.text}')
        return down_speed.text, up_speed.text

    def tweet_at_provider(self, message):
        twitter_url = "https://twitter.com/home"
        self.driver.get(twitter_url)

        time.sleep(3)
        username = self.driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'
        )
        username.send_keys(self.twitter_username, Keys.ENTER)
        time.sleep(1)

        password = self.driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
        )
        password.send_keys(self.twitter_password, Keys.ENTER)
        time.sleep(5)

        post = self.driver.find_element(
            By.XPATH,
            value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div'
        )
        post.send_keys(message)

        time.sleep(1)
        post_button = self.driver.find_element(
            By.XPATH,
            value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span'
        )
        post_button.click()

        time.sleep(3)
        print('Message posted.')
