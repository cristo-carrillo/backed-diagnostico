import os
import ssl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(email_receptor, mail_emisor):
    try:
        contexto =  ssl.create_default_context()
        session_email = smtplib.SMTP_SSL('smtp.gmail.com', 465, context = contexto)
        session_email.login(os.getenv('EMAIL'), os.getenv('PASSWORD_EMAIL'))
        print(session_email.sendmail(os.getenv('EMAIL'), email_receptor, body_email(email_receptor,mail_emisor)))
        session_email.quit()
        return {"cod":"00"}
    except Exception as e:
        return {"cod":f"500 {e}"}

def body_email(email_receptor, mail_emisor):
    
    asunto = 'Conoce la probabilidad de padecer diabetes'
    body = f"""
    <div class="banner" >
        <div class="contenido" >
            
            <h1>Diagnosticate</h1>
            <p>A {mail_emisor} le preocupa tu salud, Conoce la probabilidad de padecer diabetes.</p>
            <p>"Conocer la diabetes es el primer paso hacia la prevención, el diagnóstico y el tratamiento"</p>
            <div>
                <p> https://diagnosis-diabetes.netlify.app/inicio</p>
            </div>
        </div>
        <img src="https://i.postimg.cc/Y0QTL4mr/icono-dia.png" type="image/png">
    </div>
    """
    msg = MIMEMultipart('alternative')
    msg['Subject'] = asunto
    msg['From'] = os.getenv('EMAIL')
    msg['To'] = email_receptor
    part2 = MIMEText(body, 'html')
    msg.attach(part2)
    
    
    return msg.as_string()
