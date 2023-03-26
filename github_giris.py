
from email.message import EmailMessage
import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
email_sender="oguztizlak@gmail.com"
email_password="fsveigynlbjzljub"
email_recevier="oguztizlak@gmail.com"
subject="deneme"
body="""
deneme mail gonderme
"""
em=EmailMessage()
em["from"]=email_sender
em["to"]=email_recevier
em["subject"]=subject
em.set_content(body)
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
  smtp.login(email_sender,email_password)
  smtp.sendmail(email_sender,email_recevier,em.as_string())

