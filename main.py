import os
import csv
import smtplib
import logging
from datetime import datetime
from email.message import EmailMessage

# ==========================
# CONFIGURAÇÕES GERAIS
# ==========================
MODO_TESTE = True  # ⬅️ Altere para False para enviar e-mails de verdade 🚀
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, f"execucao_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

remetente = os.environ.get("EMAIL_USER")
senha = os.environ.get("EMAIL_PASS")
csv_file = "data/destinatarios.sample.csv"

# ==========================
# CONFIGURAÇÃO DO LOG
# ==========================
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Também exibe no terminal
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console.setFormatter(formatter)
logging.getLogger().addHandler(console)

# ==========================
# FUNÇÃO DE ENVIO DE E-MAIL
# ==========================
def enviar_email(nome, destinatario):
    msg = EmailMessage()
    msg["Subject"] = "Exemplo de automação de e-mail com Python"
    msg["From"] = remetente
    msg["To"] = destinatario
    msg.set_content(f"Olá {nome},\n\nEste é um teste de automação de e-mails em Python.\n\nAbraços,\nEquipe IA")

    if MODO_TESTE:
        logging.info(f"[TESTE] Simulação de envio para {nome} ({destinatario}) ✅")
    else:
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
                servidor.login(remetente, senha)
                servidor.send_message(msg)
                logging.info(f"E-mail enviado com sucesso para {nome} ({destinatario}) 📤")
        except Exception as e:
            logging.error(f"Erro ao enviar para {nome} ({destinatario}): {e}")

# ==========================
# EXECUÇÃO PRINCIPAL
# ==========================
if not os.path.exists(csv_file):
    logging.warning(f"Arquivo '{csv_file}' não encontrado. Nenhum e-mail será processado.")
    logging.info("💡 Dica: Crie o arquivo 'data/destinatarios.sample.csv' com colunas 'nome' e 'email'.")
else:
    with open(csv_file, newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            nome = linha["nome"]
            destinatario = linha["email"]
            enviar_email(nome, destinatario)

logging.info("✅ Execução finalizada com segurança.")
logging.info(f"🔧 Modo atual: {'TESTE (sem envio real)' if MODO_TESTE else 'ENVIO REAL (e-mails sendo disparados!)'}")
logging.info(f"🗂️ Log salvo em: {LOG_FILE}")

