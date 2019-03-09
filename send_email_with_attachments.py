##https://github.com/TeCoEd/Whats-News/tree/master/Code
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders 
from config  import EMAIL_ADDRESS,PASSWORD,toaddr_s
import os 

def send_an_email(file_name,subject="sending email with attachments",\
            body='from Python!'):
   
   
    me =  EMAIL_ADDRESS
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = me
    msg.preamble = "test " 
    msg.attach(MIMEText(body,'plain'))

    part = MIMEBase('application', "octet-stream")

    part.set_payload(open(file_name, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename=' + file_name.split("/")[-1])
    msg.attach(part)


    try:
       s = smtplib.SMTP('smtp.gmail.com', 587)
       s.ehlo()
       s.starttls()
       s.ehlo()
       s.login(EMAIL_ADDRESS, PASSWORD)
       #s.send_message(msg)
       aa=[s.sendmail(me, toaddr, msg.as_string()) for toaddr in toaddr_s]
       s.quit()
  
    except Exception as e:
          print (e)
    finally:
        pass
          

def send_an_email_to_visitor(file_name,Visitor_email,subject="sending email with attachments",\
            body='from Python!'):
   
    toaddr_s = []
    toaddr_s.append(Visitor_email)
    me =  EMAIL_ADDRESS
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = me
    msg.preamble = "test " 
    msg.attach(MIMEText(body,'plain'))

    part = MIMEBase('application', "octet-stream")

    
    part.set_payload(open(file_name, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename=' + file_name.split("/")[-1])
    # msg.attach(part)


    try:
       s = smtplib.SMTP('smtp.gmail.com', 587)
       s.ehlo()
       s.starttls()
       s.ehlo()
       s.login(EMAIL_ADDRESS, PASSWORD)
       #s.send_message(msg)
       aa=[s.sendmail(me, toaddr, msg.as_string()) for toaddr in toaddr_s]
       s.quit()
    
    except Exception as e:
          print (e)
    finally:
        pass
