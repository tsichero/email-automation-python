import os
import smtplib
from email.mime.text import MIMEText

# Pega os dados do ambiente configurados nos Secrets do GitHub
remetente = os.getenv("SMTP_USER")
senha = os.getenv("SMTP_PASS")

# Define destinatário e mensagem
destinatario = "contasintelligence@gmail.com"  # ou outro e-mail pra testar
mensagem = MIMEText("Teste de envio automático com GitHub Actions 🚀")
mensagem["Subject"] = "Automação de E-mail com Python"
mensagem["From"] = remetente
mensagem["To"] = destinatario

# Envia o e-mail
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
    servidor.login(remetente, senha)
    servidor.send_message(mensagem)

print("✅ E-mail enviado com sucesso!")
