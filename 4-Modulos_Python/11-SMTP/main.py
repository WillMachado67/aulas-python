import os
import pathlib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from dotenv import load_dotenv  # type: ignore

load_dotenv()

# Caminho HTML
CAMINHO_HTML = pathlib.Path(__file__).parent / 'email.html'

# Dados do remetente e destinatario
remetente = os.getenv('FROM_EMAIL', '')
destinatario = "machado.willian.av@gmail.com"

# Cinfigurações SMTP
smtp_sever = os.getenv('SMTP_SEVER', '')
smtp_port = os.getenv('SMTP_PORT', '')
smtp_user_name = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Menssagem de texto
with open(CAMINHO_HTML, 'r') as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='Antonio')

# print(texto_email)

# transformar nossa menssagem em MIMEmultpart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Meu primeio E-mail com python'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

# Envia o email
with smtplib.SMTP(smtp_sever, smtp_port) as sever:
    sever.ehlo()
    sever.starttls()
    sever.login(smtp_user_name, smtp_password)
    sever.send_message(mime_multipart)
    print('E-mail enviado.')
