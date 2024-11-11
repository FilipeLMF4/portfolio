import smtplib

from twilio.rest import Client


class NotificationManager:

    def __init__(self):
        self.ACCOUNT_SSID = "SSID"
        self.AUTH_TOKEN = "Token"

    def send_message(self, mess):
        client = Client(self.ACCOUNT_SSID, self.AUTH_TOKEN)
        message = client.messages.create(
            body=mess,
            from_='phone number',
            to='phone number'
        )
        print(message.status)

    def send_emails(self, message, mail_list):
        app_pass = "password"
        my_email = "email"

        for mail in mail_list:
            user_email = mail["email"]
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=app_pass)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=user_email,
                    msg=f"Subject: Check out this flight deal!\n\n{message}".encode('utf-8')
                )
