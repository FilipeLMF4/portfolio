# import smtplib
#
# APP_PASS = "byekjbwklgkcfgxp"
# my_email = "feftestmail4@gmail.com"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # No need to close connection this way
#     connection.starttls()  # Makes connection secure
#     connection.login(user=my_email, password=APP_PASS)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="feftestmailyh@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )

# import datetime as dt
#
# now = dt.datetime.now()  # Datetime
# year = now.year  # Integer
# month = now.month  # Also has day, minute, second, microsecond
#
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1996, month=1, day=14, minute=30)
# print(date_of_birth)


import smtplib
import datetime as dt
import random

APP_PASS = "Your Password"
my_email = "Your Email"

day_of_week = dt.datetime.now().weekday()

# Send motivational quote every monday
if day_of_week == 0:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()

    quote_to_send = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # No need to close connection this way
        connection.starttls()  # Makes connection secure
        connection.login(user=my_email, password=APP_PASS)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="feftestmailyh@yahoo.com",
            msg="Subject:Motivational Quote\n\n" + quote_to_send
        )
