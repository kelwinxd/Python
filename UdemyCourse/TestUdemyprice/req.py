import requests
import json
from email.mime.text import MIMEText
import time
import smtplib
from email.mime.text import MIMEText


url = 'https://www.udemy.com/api-2.0/courses/the-complete-javascript-course/'

header = {
  "Accept": "application/json, text/plain, */*",
  "Authorization": "Basic RnhZdUtGS094aDhFdzhZZmMwT0pKSXc2R1pWbVNhMkM4M1FWTnp5dTpzcGlkZXJtZW0zMjE=",
  "Content-Type": "application/json"
}

def enviar_email(value):
    # Configurações do servidor SMTP do Hotmail/Outlook
    smtp_server = 'smtp.live.com'
    smtp_port = 587
    smtp_username = 'kelwin_esechiel@hotmail.com'
    smtp_password = 'myheart123'

    # Criação do objeto SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    # Autenticação no servidor SMTP
    server.login(smtp_username, smtp_password)

    # Criação da mensagem de e-mail
    remetente = 'kelwin_esechiel@hotmail.com'
    destinatario = 'kelwin.esechiel@hotmail.com'
    assunto = 'Teste'
    corpo_mensagem = f'O valor é esse bixo, está {value}!!'

    mensagem = MIMEText(corpo_mensagem)
    mensagem['From'] = remetente
    mensagem['To'] = destinatario
    mensagem['Subject'] = assunto

    # Envio do e-mail
    server.sendmail(remetente, destinatario, mensagem.as_string())

    # Encerramento da conexão SMTP
    server.quit()




while True:

 response = requests.get(url, headers=header)



 price = response.json()['price']
 priceEdit = json.dumps(price).replace('R$','').strip()
 objPrice = json.loads(priceEdit)
 floatP = float(objPrice)

 if floatP < 180:
    enviar_email(floatP)

 print(floatP)
 time.sleep(5)
 
 


