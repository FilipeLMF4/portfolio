from twilio.rest import Client


class NotificationManager:

    def __init__(self):
        self.ACCOUNT_SSID = "SSID"
        self.AUTH_TOKEN = "Token"

    def send_message(self, mess):
        client = Client(self.ACCOUNT_SSID, self.AUTH_TOKEN)
        message = client.messages.create(
            body=mess,
            from_='Phone number',
            to='Phone number'
        )
        print(message.status)
