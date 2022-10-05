
# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=1988, month=2, day=28)
# print(date_of_birth)

# dict_of_quotes= {}
# for q in list_of_quotes:
#     a = q.split('-')
#     dict_of_quotes[a[1].strip()] = a[0]



# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs=to_address, 
#                         msg='Subject:hej hi hello\n\nwith yo yo yo')

import smtplib
import random
import datetime as dt

with open('quotes.txt', 'r') as q:
    list_of_quotes = [quote for quote in q.readlines()]

random_quote = random.choice(list_of_quotes)
auth_and_quote = random_quote.split('-')
auth = auth_and_quote[1].strip()
quote = auth_and_quote[0]

my_email = 'lucjanoforpythono@gmail.com'
password = 'tylazhlsxqkujcth'
to_address = 'lucjanopavarotti@yahoo.com'

now = dt.datetime.now()
print(now.weekday())

if now.weekday() == 2:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_address, msg=f"Subject:{auth}\n\n{quote}")