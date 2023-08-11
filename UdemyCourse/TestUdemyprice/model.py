import smtplib
from email.mime.text import MIMEText




def enviar_email():
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
    corpo_mensagem = 'O valor é esse bixo'

    mensagem = MIMEText(corpo_mensagem)
    mensagem['From'] = remetente
    mensagem['To'] = destinatario
    mensagem['Subject'] = assunto

    # Envio do e-mail
    server.sendmail(remetente, destinatario, mensagem.as_string())

    # Encerramento da conexão SMTP
    server.quit()
