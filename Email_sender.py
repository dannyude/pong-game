from email.message import EmailMessage
import ssl 
import smtplib #server responsible for sending mail, to people.(simple mail transfer protocol)
#acronym (Sending, Mail To People.)

email_sender = "danielude61@gmail.com"#
email_password = "bsffsgszmehrcyhh"
smtp_server = "smtp.gmail.com"
email_reciever = "tamed29101@ngopy.com"# person recieving the email

subject = "How to create an automated python program" #subect of the email
body =   """
The body of the email, has to be opened with three quotes instead of two.
"""
""" The next thing you want to is to create an instance of the email library, instance.
And to do so, you do 'em = Emailmessage'. You want to also instantiaite the email sender,the
email reciever,subject and body.
""" 
em = EmailMessage()

em ["From"]= email_sender
em ["To"]= email_reciever
em ["Subject"]= subject

em.set_content(body)#this is how you initialise the body of the Email.

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, 465, context=context) as server: #makes the server secure.
    server.login(email_sender, email_password)
    server.sendmail(email_sender, email_reciever, em.as_string())#what this is doing is that it is
    #converting the email sender and the email reciever as strings.
