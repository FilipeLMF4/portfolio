# ----------------------- Extra Hard Starting Project ------------------------ #
import smtplib
import datetime as dt
import pandas as pd
import os
import random

APP_PASS = "Your Password"
my_email = "Your Email"

# 1. Update the birthdays.csv
all_birthdays = pd.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
today_month = dt.datetime.now().month
today_day = dt.datetime.now().day

birthdays_today = all_birthdays[(all_birthdays.month == today_month) & (all_birthdays.day == today_day)]

# 3. If step 2 is true, pick a random letter from letter templates
# and replace the [NAME] with the person's actual name from birthdays.csv
if len(birthdays_today) > 0:
    for index, row in birthdays_today.iterrows():
        name_b = row["name"]
        letter_template = random.choice(os.listdir("letter_templates"))
        with open(f"letter_templates/{letter_template}") as file:
            letter = file.read()

        custom_letter = letter.replace("[NAME]", name_b)

# 4. Send the letter generated in step 3 to that person's email address.
        email_b = row.email
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # No need to close connection this way
            connection.starttls()  # Makes connection secure
            connection.login(user=my_email, password=APP_PASS)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email_b,
                msg=f"Subject:Happy Birthday, {name_b}!\n\n{custom_letter}"
            )

# To run code in cloud: https://www.pythonanywhere.com
