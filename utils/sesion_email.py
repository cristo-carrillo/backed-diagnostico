import ssl
import smtplib
import os
class session_activa:
    session_email = ""
    def __init__(self):
        contexto =  ssl.create_default_context()
        session_activa.session_email = smtplib.SMTP_SSL('smtp.gmail.com', 465, context = contexto)
        session_activa.session_email.login(os.getenv('EMAIL'), os.getenv('PASSWORD_EMAIL'))