import getpass
import smtplib
from email.mime.text import MIMEText

print('--------------------------------------------------')
print('        E-mail spammer!\n')
print('If you use a google email\nyou need to allow less secure app access at\n\nhttps://myaccount.google.com/u/0/security?hl=pt:')
print('--------------------------------------------------')


# conexão com os servidores do google
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465
# username ou email para logar no servidor
username = input('Type your e-mail: ')
password = getpass.getpass('Your password: ')

mail_from = input('Destination e-mail: ')
mail_to = [mail_from]

mail_title = input('Title of e-mail: ')
mail = input('Type the e-mail: ')
try:
    mail_amount = int(input('How many emails do you want to send: '))

    i = 0

    while i <= mail_amount: 
        # email que vai ser enviado
        message = MIMEText(mail) # email 
        message['subject'] = mail_title # título do e-mail
        message['from'] = mail_from
        message['to'] = ', '.join(mail_to)

        # conectaremos de forma segura usando SSL
        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)

        # fazer login nele
        server.login(username, password)
        server.sendmail(mail_to, mail_from, message.as_string())
        server.quit()

        i += 1

except ValueError:
    print('Type only numbers!')
