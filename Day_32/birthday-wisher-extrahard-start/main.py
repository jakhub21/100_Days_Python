import datetime as dt
import pandas as pd
import random
import smtplib
import os
##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

my_email = os.environ.get('STMPLIB_EMAIL')
password = os.environ.get('STMPLIB_PASSWORD')

file = pd.read_csv("birthdays.csv")
birthday_dict = {(file_row["month"], file_row["day"]): file_row for (index, file_row) in file.iterrows()}
now = dt.datetime.now()
tuple_today = (now.month, now.day)

if tuple_today in birthday_dict:
    letter_num = random.randint(1, 3)
    birthday_person = birthday_dict[tuple_today]
    with open(f"letter_templates/letter_{letter_num}.txt", "r") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", birthday_person["name"])
    with open(r'SampleFile.txt', 'w') as file:
        file.write(letter)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="jakhub21@gmail.com",
                            msg=f"Subject:Happy Birthday!\n\n{letter}")





