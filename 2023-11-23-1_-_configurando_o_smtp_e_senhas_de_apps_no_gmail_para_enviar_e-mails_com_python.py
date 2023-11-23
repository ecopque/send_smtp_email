import os #1:
from dotenv import main
import pathlib #Path
import string #Template
import datetime #datetime
from email.mime.multipart import MIMEMultipart #8: #9:
from email.mime.text import MIMEText #10:
# import email.mime #7:
import smtplib #16:

main.load_dotenv() #2:
remetente  = os.getenv('FROM_EMAIL', '') #3:
destinatario = remetente #4:

smtp_server_google = 'smtp.gmail.com'
smtp_port_google = 587
smtp_username_google = os.getenv('FROM_EMAIL', '') #6:
smtp_password_google = os.getenv('EMAIL_PASSWORD', '') #5:

CAMINHO_TXT = pathlib.Path(__file__).parent / 'file100.txt'
with open(CAMINHO_TXT, 'r') as arquivo:
    leitura = arquivo.read()
    modelo_padrao = string.Template(leitura)
    data_atual = datetime.datetime.today().strftime('%d/%m/%Y')
    dicionario = dict(nome='Edson', valor='R$ 100,00',
                data=data_atual, telefone='+55 71 999-888-777',
                email='contact@ibm.com', empresa='IBM')
    texto_definitivo = modelo_padrao.safe_substitute(dicionario) #13:
# print(texto_email)

mime_multipart = MIMEMultipart() #14:
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'E-mail automatizado (Python)'

corpo_email = MIMEText(texto_definitivo, 'plain', 'utf-8') #11: #12:
mime_multipart.attach(corpo_email) #15:

with smtplib.SMTP(smtp_server_google, smtp_port_google) as server: #17:
    server.ehlo() #18:
    server.starttls() #19:
    server.login(smtp_username_google, smtp_password_google) #20:
    server.send_message(mime_multipart) #21:
    print('E-mail enviado com sucesso!')


#1: Vou precisar das informações do meu ".env".
#2: Lembrando que não consegui importar o "load_dotenv".
#3: Se a variável de ambiente não estiver definida, o segundo argumento é retornado como um valor padrão (string vazia).
#4: O destinatário será o remetente.
#5: Está buscando a senha dentro do ".env".
#6: Está buscando o login dentro do ".env".
#7: "email" é biblioteca principal e "mime" é um submóduo dentro dela.
#8: É usada para criar mensagens de e-mail MIME multipart.
#9: O MIME (Multipurpose Internet Mail Extensions) é um padrão da Internet que estende o formato de e-mail para suportar mensagens de texto em caracteres não-ASCII, além de outros tipos de dados como imagens, áudio e vídeo. O MIME permite que os e-mails contenham diferentes partes, cada uma com seu próprio tipo de conteúdo. A classe MIMEMultipart é usada para criar mensagens de e-mail que consistem em várias partes. Por exemplo, você pode ter uma parte de texto, uma parte HTML e vários anexos em uma única mensagem.
#10: A classe MIMEText é comumente usada quando você deseja incluir uma parte de texto simples em sua mensagem de e-mail, seja como corpo da mensagem ou parte de um corpo mais complexo se a mensagem for multipart.
#11: Criando uma instância para repsentar a parte do texto do corpo do e-mail, onde "plain" indica que o conteúdo do e-mail é texto simples. Outra opção comum seria 'html' se você estivesse formatando o corpo do e-mail como HTML.
#12: Especifica a codificação do texto. 'utf-8' é uma escolha comum para suportar caracteres Unicode.
#13: Substitui variáveis no modelo (template/modelagem) pelos valores fornecidos no dicionário "dados" (sem lançar exceção).
#14: Permite adicionar uma parte de texto usando MIMEText e uma parte de anexo usando MIMEBase, e, em seguida, adicioná-las ao objeto MIMEMultipart. Isso permite a criação de e-mails mais complexos com várias partes.
#15: Será utilizado para anexar o conteúdo de "corpo_email/MIMEText" ao MIMEMultipart().
#16: Essa biblioteca fornece uma interface para enviar e-mails usando o protocolo SMTP.
#17: "smtplib.SMTP" é uma classe que representa uma conexão com um servidor SMTP.
#18: "ehlo()" é usado para cumprimentar o servidor SMTP. Significa: "Extended Hello". Ele é um passo inicial onde o cliente (seu código) comunica ao servidor que ele pretende usar extensões específicas.
#19: Inicia uma camada de segurança TLS na conexão SMTP.
#20: Realizando login.
#21: Comando para enviar e-mail.

#Link Google: https://support.google.com/accounts/answer/185833?hl=pt-BR
#Link2 Google: https://myaccount.google.com/security