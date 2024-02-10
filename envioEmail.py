import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email(assunto, corpo, destinatario):
    remetente = "seuEmail@email.com"
    senha = "suaSenhaAppEmail"
    
    # Configuração da mensagem
    mensagem = MIMEMultipart()
    mensagem['From'] = remetente
    mensagem['To'] = destinatario
    mensagem['Subject'] = assunto

    # Adicionando o corpo do e-mail
    mensagem.attach(MIMEText(corpo, 'plain'))

    # Conectando ao servidor SMTP do Gmail
    servidor_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    servidor_smtp.starttls()  # Inicia a criptografia TLS
    servidor_smtp.login(remetente, senha)  # Login no servidor SMTP

    # Enviando o e-mail
    texto_email = mensagem.as_string()
    servidor_smtp.sendmail(remetente, destinatario, texto_email)

    # Encerrando a conexão com o servidor SMTP
    servidor_smtp.quit()

# Exemplo de uso
assunto = "Teste de e-mail com Python"
corpo = "Olá! Este é um e-mail de teste enviado via Python."
destinatario = "Destinatario@email.com"

enviar_email(assunto, corpo, destinatario)
