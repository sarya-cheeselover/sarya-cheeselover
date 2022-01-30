#!/usr/bin/env python3
import smtplib


username = "name@email.com"
password = input("type in the password please: ") #or hard-enter your password.. there are couple of options here.

sent_from = 'sender@email.com'
to = ['reciepant@email.com']
subject = 'OMG I DID IT!'
body = 'Heey heeey duuude \n This is script, sarya created me to send you an email!'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from,", ".join(to),subject,body)

### until here I think it should be clear what is it for.


try:

    server = smtplib.SMTP_SSL("smtp.gmail.com",465) ###create an instance of SMTP_SSL() class and pass the server name and port number
    print (server) ###step I added to test if connection is working
    server.ehlo() ### say hi to the server... exchange creditioanl
    server.login(username,password) ###take wild guess... yep it's log in the account we be sending emails from.
    server.sendmail(sent_from, to, email_text) ### again, take a guess. careful the parameter order
    server.close() ###important, like opening files you don't want to keep them opened.

    print ('Email has been sent!')
except:
    print ("something went wrong")
