import pandas, random, smtplib
import datetime as dt

my_email = 'lucjanoforpythono@gmail.com'
password = 'tylazhlsxqkujcth'

def today_day_func():
    now = dt.datetime.now()
    today_day = now.day
    today_month = now.month
    today = (today_month, today_day)
    return today

def sending_email(row, contents):            
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=row.email, msg=f"Subject:Happy Birthday!\n\n{contents}")

def creating_letter(row):
    letter_no = random.randint(1, 3)
    with open(f"letter_{letter_no}.txt") as letter:
        contents = letter.read()
        contents = contents.replace('[NAME]', row.names)
    return contents

def main(today):
    data = pandas.read_csv('birthdays.csv')
    df = pandas.DataFrame(data)
    for index, row in df.iterrows():
        if (row.month, row.day) == today:
            contents = creating_letter(row)
            sending_email(row, contents)

today = today_day_func()

main(today)
