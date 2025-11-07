import os
import smtplib
from email.message import EmailMessage

# Pega as variáveis de ambiente definidas no GitHub Actions
remetente = os.environ.get("EMAIL_USER")
senha = os.environ.get("EMAIL_PASS")

# Verificação de segurança
if not remetente or not senha:
    raise ValueError("EMAIL_USER ou EMAIL_PASS não estão definidos!")

# Configura a mensagem
msg = EmailMessage()
msg["Subject"] = "Teste de envio"
msg["From"] = remetente
msg["To"] = "destinatario@exemplo.com"  # substitua pelo e-mail que quer receber
msg.set_content("Olá! Este é um teste de envio de e-mail pelo Gmail SMTP.")

# Envio do e-mail com tratamento de erros
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


