import os
import smtplib
from email.message import EmailMessage

# Pegando as variáveis de ambiente
remetente = os.environ.get(''contasintelligence@gmail.com'')
senha = os.environ.get("yxodmhdijajslsei")  # senha de app do Gmail

if not remetente or not senha:
    raise ValueError("EMAIL_USER ou EMAIL_PASS não estão definidos!")

# Configurando a mensagem
msg = EmailMessage()
msg["Subject"] = "Teste de envio"
msg["From"] = remetente
msg["To"] = "destinatario@exemplo.com"
msg.set_content("Olá! Este é um teste de envio de email pelo Gmail SMTP.")

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
        servidor.starttls()  # ativa criptografia
        servidor.login(remetente, senha)
        servidor.send_message(msg)
        print("Email enviado com sucesso!")
except smtplib.SMTPAuthenticationError:
    print("Erro de autenticação: verifique EMAIL_USER e EMAIL_PASS (senha de app do Gmail).")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

