from email.message import EmailMessage
import smtplib, ssl


sender = '<enter your password>'
password = 'you pass or api key'

receiver = '<receiver or recievers>'

em = EmailMessage()
em['From'] = sender
em['To'] = receiver
em['Subject'] = 'Test'
em.set_content('This is a test')

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, em.as_string())
    
