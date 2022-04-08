"""Sending email by using python"""

import smtplib
server = smtplib.SMTP("smpt.gmail.com", 587)
server.starttls()

server.login("nacati.sakir.74", password)
message = "\n bu benim son python dersim"
mails = ["kmtayana3860@gmail.com" , 
        "tarknsahin@gmail.com", 
        "sfrancisclarus@gmail.com"]
server.sendmail("necati.sakir.74@gmail.com", mails, message)
server.quit01~
