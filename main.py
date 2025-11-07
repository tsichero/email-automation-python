import os
import smtplib
from email.message import EmailMessage

# Pega os valores do secret (não coloque e-mail ou senha no código!)
remetente = os.environ.get("EMAIL_USER")
senha = os.environ.get("EMAIL_PASS")

# Configura o e-mail
destinatario = "destino@example.com"  # coloque o e-mail de destino real
mensagem = EmailMessage()
mensagem.set_content("Olá! Teste de envio de e-mail via Python.")
mensagem["Subject"] = "Teste de Envio"
mensagem["From"] = remetente
mensagem["To"] = destinatario

# Conecta ao servidor SMTP e envia
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
        servidor.login(remetente, senha)
        servidor.send_message(mensagem)
    print("E-mail enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar e-mail: {e}")


