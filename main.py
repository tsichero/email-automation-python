import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Variáveis seguras (vindas do GitHub Secrets)
remetente = os.environ.get("EMAIL_USER")
senha = os.environ.get("EMAIL_PASSWORD")

# Destinatário
destinatario = " contasintelligence@gmail.com"

# Mensagem
mensagem = MIMEMultipart()
mensagem["From"] = remetente
mensagem["To"] = destinatario
mensagem["Subject"] = "Automação de E-mail com Python 🚀"

corpo = "Olá! Este é um e-mail automático enviado pelo GitHub Actions usando Python 😺"
mensagem.attach(MIMEText(corpo, "plain"))

# Conexão segura com o servidor SMTP do Gmail
with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
    servidor.starttls()
    servidor.login(remetente, senha)
    servidor.send_message(mensagem)

print("✅ E-mail enviado com sucesso!")
