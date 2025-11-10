import os
import csv
import smtplib
import logging
from datetime import datetime
from email.message import EmailMessage

# ==========================
# CONFIGURAÇÕES GERAIS
# ==========================
MODO_TESTE = True  # ⬅️ Altere para False para enviar e-mails reais 🚀
LOG_DIR = "logs"
MAX_LOGS = 10  # número máximo de arquivos de log mantidos

remetente = os.environ.get("EMAIL_USER")
senha = os.environ.get("EMAIL_PASS")
csv_file = "data/destinatarios.sample.csv"

# ==========================
# CONFIGURAÇÃO DE LOG
# ==========================
os.makedirs(LOG_DIR, exist_ok=True)

# Define nome do log com data e modo (TESTE ou REAL)
status_execucao = "TESTE" if MODO_TESTE else "REAL"
LOG_FILE = os.path.join(
    LOG_DIR,
    f"execucao_{status_execucao}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
)

# Configura o logger
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Exibe logs também no terminal
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console.setFormatter(formatter)
logging.getLogger().addHandler(console)

logging.info("🚀 Iniciando execução do script de automação de e-mails...")
logging.info(f"📂 Log sendo salvo em: {LOG_FILE}")
logging.info(f"🔧 Modo atual: {status_execucao}")

# ==========================
# FUNÇÕES AUXILIARES
# ==========================

def limpar_logs_antigos():
    """Remove logs antigos, mantendo apenas os mais recentes."""
    logs = sorted(
        [os.path.join(LOG_DIR, f) for f in os.listdir(LOG_DIR) if f.endswith(".log")],
        key=os.path.getmtime,
        reverse=True
    )
    for antigo in logs[MAX_LOGS:]:
        os.remove(antigo)
        logging.info(f"🧹 Log antigo removido: {os.path.basename(antigo)}")

def enviar_email(nome, destinatario):
    """Envia ou simula o envio de e-mails."""
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
total = 0
sucesso = 0

if not os.path.exists(csv_file):
    logging.warning(f"⚠️ Arquivo '{csv_file}' não encontrado. Nenhum e-mail será processado.")
    logging.info("💡 Dica: Crie o arquivo 'data/destinatarios.sample.csv' com colunas 'nome' e 'email'.")
else:
    with open(csv_file, newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            total += 1
            nome = linha["nome"]
            destinatario = linha["email"]
            enviar_email(nome, destinatario)
            sucesso += 1

# ==========================
# RESUMO FINAL
# ==========================
logging.info("✅ Execução finalizada com segurança.")
logging.info(f"📊 Total de registros processados: {total}")
logging.info(f"📩 E-mails {'simulados' if MODO_TESTE else 'enviados'} com sucesso: {sucesso}")
logging.info(f"🗂️ Log salvo em: {LOG_FILE}")

# Limpa logs antigos
limpar_logs_antigos()

print("\n✨ Execução concluída! Veja o log completo em:")
print(LOG_FILE)


