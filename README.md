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


O e-mail será enviado para o destinatário especificado.

## Nota
Para contas do Gmail, é necessário permitir o acesso a aplicativos menos seguros ou gerar uma senha específica de aplicativo. Siga as instruções do Google para fazer isso.

## Contribuição
Contribuições são bem-vindas! Abra uma issue ou envie um pull request com melhorias.

## Licença
Este projeto está licenciado sob a Licença MIT.

Este README.md fornece instruções sobre como usar o script, configuração necessária e notas importantes. Certifique-se de incluir um arquivo LICENSE no seu repositório se desejar atribuir uma licença específica ao seu código.



# Automação de Envio de Email Agendado

Este projeto consiste em um script Python para automatizar o envio de emails agendados a cada duas semanas.

## Descrição

O script utiliza a biblioteca `smtplib` para enviar emails através de um servidor SMTP. Ele também faz uso da biblioteca `APScheduler` para agendar o envio dos emails a cada duas semanas.

## Funcionalidades

- Envia emails automaticamente a cada duas semanas.
- Pode ser configurado para enviar para múltiplos destinatários.
- Permite personalizar o conteúdo e o assunto do email.

## Pré-requisitos

- Python 3 instalado no ambiente.
- Conta de email válida para envio dos emails.
- Permissões de acesso à conta de email para envio.



