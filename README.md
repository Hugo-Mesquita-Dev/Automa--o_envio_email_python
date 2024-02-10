# Automatização de Envio de E-mails em Python

Este script em Python permite automatizar o envio de e-mails utilizando a biblioteca `smtplib` para se conectar a um servidor SMTP (Simple Mail Transfer Protocol).

## Requisitos

- Python 3.x
- Conta de e-mail (por exemplo, Gmail)

## Instalação

Não há necessidade de instalar bibliotecas adicionais. A biblioteca `smtplib` já está incluída na biblioteca padrão do Python.

## Configuração

1. Clone ou baixe este repositório para o seu computador.
2. Abra o arquivo `enviar_email.py` em um editor de texto.
3. Edite as seguintes variáveis no código:
    - `remetente`: Endereço de e-mail do remetente.
    - `senha`: Senha da conta de e-mail do remetente ou senha específica de aplicativo.
    - `assunto`: Assunto do e-mail que deseja enviar.
    - `corpo`: Corpo do e-mail que deseja enviar.
    - `destinatario`: Endereço de e-mail do destinatário.
4. Salve as alterações.

## Uso

Execute o script `enviar_email.py` no seu terminal:

```bash
python enviar_email.py
