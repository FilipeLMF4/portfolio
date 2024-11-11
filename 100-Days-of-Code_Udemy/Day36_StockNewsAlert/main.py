import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# AlphaVantage
API_KEY_AV = "API Key"
AV_ENDPOINT = "https://www.alphavantage.co/query"
AV_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY_AV,
}

# NewsApi
API_KEY_NEWS = "API Key"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_PARAMS = {
    "q": COMPANY_NAME,
    "searchin": "title",
    "language": "en",
    "pageSize": 3,
    "apiKey": API_KEY_NEWS
}

# Twillio
ACCOUNT_SSID = "Account SSID"
AUTH_TOKEN = "Token"


def get_price_change():
    av_response = requests.get(AV_ENDPOINT, AV_PARAMS)
    av_response.raise_for_status()
    av_data = av_response.json()["Time Series (Daily)"]
    av_data_list = [value for (key, value) in av_data.items()]
    closing_price = float(av_data_list[0]["4. close"])
    previous_closing_price = float(av_data_list[1]["4. close"])

    price_change = round((closing_price - previous_closing_price)/previous_closing_price*100, 3)
    return price_change


def get_news():
    news_response = requests.get(NEWS_ENDPOINT, NEWS_PARAMS)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
    for news in news_data:
        send_message(news)


def send_message(message_data):
    symbol = "🔺"
    global change
    if change < 0:
        symbol = "🔻"

    formatted_message = (f"{STOCK}: {symbol}{abs(change)}%\n"
                         f"Headline: {message_data['title']}\n"
                         f"Brief: {message_data['description']}"
                         )

    client = Client(ACCOUNT_SSID, AUTH_TOKEN)
    message = client.messages.create(
        body=formatted_message,
        from_='Twillio Phone Number',
        to='Phone Number'
    )
    print(message.status)


# Main
change = get_price_change()
if abs(change) >= 5:
    get_news()
