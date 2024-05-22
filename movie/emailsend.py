from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib 
import pyotp
import config
import time

def makecode():
       
    secret = pyotp.random_base32()
    

    
    totp = pyotp.TOTP(secret,interval=60)

    
    otp = totp.now()
    return otp ,totp

   
        



def SendMail(reciveMail,code):
    message = MIMEMultipart()

    message['from'] = 'Moviebank'
    message['to']  = reciveMail
    message['subject']  = 'This is an important message'
    
    message.attach(MIMEText(f'This is your code, please do not share it with others\n\t\t{code}'))

    with smtplib.SMTP(host='smtp.gmail.com' , port=587) as smtp:
        smtp.ehlo()
        
        smtp.starttls()
        
        smtp.login(config.username ,config.password)
        
        smtp.send_message(message)
        
def checkcode(code,totp):
    if totp.verify(code):
        return True
    else:
        return False
    