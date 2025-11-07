Código em Python
# --- Configurações do e-mail ---
remetente = "SEU_EMAIL@gmail.com"           # quem envia
senha = "SENHA_DO_APP"                      # senha de app (não sua senha normal!)
destinatario = "DESTINATARIO@gmail.com"     # quem vai receber

assunto = "Teste de automação de e-mail"
mensagem = "Olá! Este é um e-mail automático enviado pelo meu projeto Python no GitHub 🚀"
# --- Conectando e enviando o e-mail ---
# Criação da estrutura do e-mail
email = MIMEMultipart()
email["From"] = remetente
email["To"] = destinatario
email["Subject"] = assunto

# Corpo da mensagem
email.attach(MIMEText(mensagem, "plain"))

try:
    # Conexão segura com o servidor do Gmail
    with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
        servidor.starttls()  # Ativa a segurança
        servidor.login(remetente, senha)  # Faz login
        servidor.send_message(email)  # Envia o e-mail
        print("✅ E-mail enviado com sucesso!")
except Exception as e:
    print("❌ Erro ao enviar o e-mail:", e)
