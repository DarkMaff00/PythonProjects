import pandas as pd
import datetime as dt
import random
import smtplib

# Your email
MY_EMAIL = ""
# Generate App password in your mailbox
PASSWORD = ""

# Add data into birthdays.csv
person_info = pd.read_csv("birthdays.csv")
now = dt.datetime.now()
today_day = now.day
today_month = now.month

for index, row in person_info.iterrows():
    if row['day'] == today_day and row['month'] == today_month:
        random_letter = random.randint(1, 3)
        with open(f"./letter_templates/letter_{random_letter}.txt") as letter:
            text = letter.read()
            text = text.replace("[NAME]", f"{row['name']}")

        # Change "smtp.gmail.com" depending on your mailbox [search for this in Internet]
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=row['email'],
                                msg=f"Subject:Happy Birthday\n\n{text}")
