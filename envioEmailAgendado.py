from apscheduler.schedulers.background import BackgroundScheduler
import time
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuração do logger
logging.basicConfig(filename='email_sender.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def enviar_email():
    remetente = "seu-email@email.com"
    senha = 'suaSenhaAppemail'
    destinatario = 'destinario@email.com'
    
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = 'Olá estarei enviando este email a cada 1 semanas, para saber como está o andamento do nosso projeto'
    corpo = 'Porfavor aguardo as atualizações do nosso projeto XperitoDaSAutomacion'
    msg.attach(MIMEText(corpo, 'plain'))

    servidor_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    servidor_smtp.starttls()
    servidor_smtp.login(remetente, senha)
    servidor_smtp.sendmail(remetente, destinatario, msg.as_string())
    servidor_smtp.quit()

    logging.info(f'E-mail enviado para {destinatario}')

def job():
    print("Tarefa agendada executada")
# Agendamento do envio de e-mail para ser executado a cada 1 hora (obs: pode alterar p/ days ou weeks)
scheduler = BackgroundScheduler()
scheduler.add_job(job, 'interval', hours=1)
scheduler.start()

try:
    while True:
        time.sleep(5) # programa será pausado por x segundos.
except KeyboardInterrupt:
    scheduler.shutdown()
