import os
from email.message import EmailMessage
import ssl
import smtplib
from dotenv import load_dotenv

load_dotenv()
def send_email(email_receptor):
    contexto =  ssl.create_default_context()
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = contexto) as smtp:
        print(os.getenv('EMAIL'))
        smtp.login(os.getenv('EMAIL'), os.getenv('PASSWORD_EMAIL'))
        smtp.sendmail(os.getenv('EMAIL'), email_receptor, body_email(email_receptor))

def body_email(email_receptor):
    asunto = 'conoce la probabilidad de padecer diabetes'
    body = """
    Ingresa al siguiente enlace y conoce la probabilidad que tienes
    de padecer diabetes
    https://diagnosis-diabetes.netlify.app/
    """
    em = EmailMessage()
    em['From'] = os.getenv('EMAIL')
    em['To'] = email_receptor
    em['Subject'] = asunto
    em.set_content(body)
    
    return em.as_string()

send_email("cjcarrillos@ufpso.edu.co")