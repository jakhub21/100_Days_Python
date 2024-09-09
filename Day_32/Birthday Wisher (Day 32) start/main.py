import smtplib
import datetime as dt
import random
import os

p = "1234ABC#$"
my_email = os.environ.get('STMPLIB_EMAIL')
password = os.environ.get('STMPLIB_PASSWORD')

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quote = quote_file.readlines()
        quote = random.choice(all_quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="jakhub21@gmail.com",
                            msg=f"Subject:Wednesday\n\n{quote}")
