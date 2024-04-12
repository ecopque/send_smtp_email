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


#1: I'll need the information from my ".env".
#2: Just a reminder that I couldn't import "load_dotenv".
#3: If the environment variable is not defined, the second argument is returned as a default value (an empty string).
#4: The recipient will be the sender.
#5: It's fetching the password from within the ".env".
#6: It's fetching the login from within the ".env".
#7: "email" is the main library and "mime" is a submodule within it.
#8: It's used to create multipart MIME email messages.
#9: MIME (Multipurpose Internet Mail Extensions) is an Internet standard that extends the email format to support text messages in non-ASCII characters, as well as other data types like images, audio, and video. MIME allows emails to contain different parts, each with its own content type. The MIMEMultipart class is used to create email messages that consist of multiple parts. For example, you can have a text part, an HTML part, and several attachments in a single message.
#10: The MIMEText class is commonly used when you want to include a simple text part in your email message, either as the body of the message or as part of a more complex body if the message is multipart.
#11: Creating an instance to represent the text part of the email body, where "plain" indicates that the email content is plain text. Another common option would be 'html' if you were formatting the email body as HTML.
#12: Specifies the encoding of the text. 'utf-8' is a common choice to support Unicode characters.
#13: Substitutes variables in the template with the values provided in the "data" dictionary (without raising an exception).
#14: Allows adding a text part using MIMEText and an attachment part using MIMEBase, and then adding them to the MIMEMultipart object. This allows the creation of more complex emails with multiple parts.
#15: Will be used to attach the content of "email_body/MIMEText" to the MIMEMultipart().
#16: This library provides an interface for sending emails using the SMTP protocol.
#17: "smtplib.SMTP" is a class that represents a connection to an SMTP server.
#18: "ehlo()" is used to greet the SMTP server. It stands for: "Extended Hello". It's an initial step where the client (your code) communicates to the server that it intends to use specific extensions.
#19: Starts a TLS security layer on the SMTP connection.
#20: Performing login.
#21: Command to send email.

#Link Google: https://support.google.com/accounts/answer/185833?hl=pt-BR
#Link2 Google: https://myaccount.google.com/security
