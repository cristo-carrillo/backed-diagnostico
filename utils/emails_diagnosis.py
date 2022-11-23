import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from utils.sesion_email import session_activa

def send_email(email_receptor):
    try:
        session_activa.session_email.sendmail(os.getenv('EMAIL'), email_receptor, body_email(email_receptor))
        return {"msg":"el familiar se ha registardo con éxito"}
    except Exception as e:
        return {"msg":"ups algo salio mal"}

def body_email(email_receptor):
    
    asunto = 'conoce la probabilidad de padecer diabetes'
    body = """
    <div class="banner" >
        <div class="contenido" >
            
            <h1>Diagnosticate</h1>
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
