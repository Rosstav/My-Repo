import time
import smtplib
import datetime

SECONDS_PER_HOUR = 3600
HOURS_PER_DAY = 24

def email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    myemail = "prtaverner@googlemail.com"
    server.login("prtaverner@googlemail.com", "")
    msg = "It's been %s days since you drank" % str((datetime.date.today()- datetime.date(2018,9,15)).days)
    server.sendmail(myemail, myemail, msg)
    server.quit()

while True:
    email()
    time.sleep(SECONDS_PER_HOUR*HOURS_PER_DAY)
