import pandas as pd
import datetime as dt
import random
import smtplib

MY_EMAIL = "intiro30@gmail.com"
PASSWORD = "qyuvalzzmvcyxqcp"

# 1. Update the birthdays.csv
data = pd.read_csv("birthdays.csv")
data_d = data.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day
today = (month, day)

for person in data_d:
    if person["month"] == month and person["day"] == day:
        file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path) as file:
            contents = file.read()
            correct = contents.replace("[NAME]", person["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=person["email"],
                                msg=f"Subject: Happy Birthday!\n\n"
                                    f"{correct}")

# birthday_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}
#
# if today in birthday_dict:
#     person = birthday_dict[today]
#     file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
#     with open(file_path) as file:
#         contents = file.read()
#         contents = contents.replace("[NAME]", person["name"])
#
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=MY_EMAIL, password=PASSWORD)
#         connection.sendmail(from_addr=MY_EMAIL,
#                             to_addrs=person["email"],
#                             msg=f"Subject: Happy Birthday!\n\n"
#                                 f"{contents}")
