import smtplib
import datetime as dt
import random

quotes_file = open("quotes.txt")
lines = quotes_file.readlines()


def email(my_email,password,quote,today):
    with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="pbelnekar04@yahoo.com",msg=f"Subject:A quote from prathamesh for {today} \n\n {quote} ")
    


def send_email():
    weekdays = ['Monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    now = dt.datetime.now()
    week_day = now.weekday()
    today_week = weekdays[week_day]
    if week_day == 0:
        random_quote = random.choice(lines)
        email("pbelnekar04@gmail.com","mtmnncoeegyoxvxx",random_quote,today_week)
        

send_email()




