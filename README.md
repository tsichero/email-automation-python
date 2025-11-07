# 📧 Automação de E-mails em Python
**Soluções profissionais de automação de e-mails** desenvolvidas em Python, ideais para empresas que buscam eficiência, segurança e escalabilidade em suas campanhas e fluxos de comunicação.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![GitHub Workflow](https://img.shields.io/badge/GitHub%20Actions-Workflow-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

Este projeto oferece uma solução completa para envio automatizado de e-mails, pensada para uso em desenvolvimento, testes e prototipagem em ambiente corporativo:
- Processamento de destinatários múltiplos via CSV  
- Uso de variáveis de ambiente para credenciais seguras  
- Suporte a e-mails de teste (FAKE) para desenvolvimento seguro — **nenhum e-mail real é enviado quando a opção de teste está ativa**  
- Estrutura modular e escalável para diferentes tipos de campanhas  
- Fácil integração com sistemas corporativos e APIs externas  

Como Funciona:
1. Clone o repositório: `git clone https://github.com/seu-usuario/email-automation-python.git && cd email-automation-python`  
2. Configure credenciais de forma segura (ou use variáveis de teste): `export EMAIL_USER="seu_email@gmail.com"` e `export EMAIL_PASS="sua_senha"`  
3. Prepare a lista de destinatários (CSV) — para testes, use e-mails FAKE conforme o padrão abaixo:  
`nome,email`  
`João,joao+test@example.com`  
`Maria,maria+test@example.com`  
4. Execute o envio automatizado: `python main.py`  

Estrutura do Projeto:
- `main.py` → Script principal  
- `destinatarios.csv` → Lista de destinatários (use e-mails FAKE em desenvolvimento)  
- `README.md` → Documentação  
- `.github/workflows/` → Testes e integração contínua  
- `secrets/` → Variáveis sensíveis (não versionado)  

Boas práticas para testes:
- Use e-mails fake (ex.: `nome+test@example.com`) em ambientes de desenvolvimento  
- Nunca commit credenciais reais no repositório  
- Valide colunas do CSV localmente antes de rodar envios em massa  

Próximos Passos:
- Integração com APIs de envio profissional (SendGrid, Mailgun, etc.)  
- Desenvolvimento de templates HTML corporativos  
- Automatização completa via GitHub Actions para fluxo contínuo  

Contato:

📧 Email: mmbjjs@gmail.com  

📞 Telefone/WhatsApp: +55 11 98841-9090  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-TainaSichero-blue?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tainã-sichero-dulcetti-65270b149)  
[![Instagram](https://img.shields.io/badge/Instagram-tataaiworld-purple?logo=instagram&logoColor=white)](https://www.instagram.com/tataaiworld/)

Entre em contato para **automatizar seus fluxos de e-mail, testar com segurança usando e-mails fake e potencializar seus resultados corporativos**.  


Licença:
MIT © Tatá Sichero


