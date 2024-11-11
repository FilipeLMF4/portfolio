import requests
from bs4 import BeautifulSoup
import smtplib

TRACKING_URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
TARGET_PRICE = 100
APP_PASS = "password"
MY_EMAIL = "email"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0",
    "Accept-Language": "en,en-US;q=0.9,pt-PT;q=0.8,pt;q=0.7"
}

response = requests.get(url=TRACKING_URL, headers=header)
soup = BeautifulSoup(response.text, 'lxml')

product_name = soup.select_one("#productTitle").getText().strip()
price = soup.select_one(".a-price .a-offscreen").getText()

price_num = float(price.split("$")[1])

if price_num <= TARGET_PRICE:
    message = f"{product_name} is now on sale for ${price_num}!\n{TRACKING_URL}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Amazon Price Alert!\n\n{message}".encode('utf-8')
        )
