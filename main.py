import os
import smtplib
import csv
from email.message import EmailMessage
from datetime import datetime

# Pega os valores do secret
remetente = os.environ.get("EMAIL_USER")
senha = os.environ.get("EMAIL_PASS")

# Caminho do CSV de destinatários
csv_file = "data/destinatarios.csv"

# Pastas de log
log_folder = "logs"
os.makedirs(log_folder, exist_ok=True)
log_sucesso = os.path.join(log_folder, "envio_sucesso.log")
log_falha = os.path.join(log_folder, "envio_falha.log")

# Função para escrever log
def log(mensagem, tipo="sucesso"):
    horario = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = f"[{horario}] {mensagem}"
    print(linha)
    arquivo_log = log_sucesso if tipo == "sucesso" else log_falha
    with open(arquivo_log, "a", encoding="utf-8") as f:
        f.write(linha + "\n")

# Função para enviar e-mail HTML
def enviar_email(nome, email, profissao):
    mensagem = EmailMessage()
    mensagem["Subject"] = "Teste de Automação Profissional"
    mensagem["From"] = remetente
    mensagem["To"] = email

    # Conteúdo HTML personalizado
    html_content = f"""
    <html>
        <body>
            <p>Olá <b>{nome}</b>,</p>
            <p>Sabemos que como <i>{profissao}</i> você vai se interessar pelo nosso conteúdo!</p>
            <p>Atenciosamente,<br>Equipe de Automação</p>
        </body>
    </html>
    """
    mensagem.add_alternative(html_content, subtype='html')

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
            servidor.login(remetente, senha)
            servidor.send_message(mensagem)
        log(f"E-mail enviado para {nome} <{email}>", "sucesso")
    except Exception as e:
        log(f"Erro ao enviar para {nome} <{email}>: {e}", "falha")

# Ler CSV e enviar e-mails
with open(csv_file, newline="", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        enviar_email(linha["nome"], linha["email"], linha["profissao"])
