import os
import csv
from datetime import datetime

# Caminho do CSV de destinatários (sample)
csv_file = "data/destinatarios.sample.csv"

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

# Função para "enviar" e-mail (simulação)
def enviar_email(dados):
    try:
        # Simula envio ao invés de enviar de verdade
        print(f"[SIMULADO] Envio de e-mail para {dados['nome']} <{dados['email']}> sobre {dados['profissao']}")
        log(f"[SIMULADO] E-mail enviado para {dados['nome']} <{dados['email']}>", "sucesso")
    except Exception as e:
        log(f"[SIMULADO] Erro ao enviar para {dados['nome']} <{dados['email']}>: {e}", "falha")

# Ler CSV e enviar e-mails (simulação)
with open(csv_file, newline="", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        enviar_email(linha)

