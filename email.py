import smtplib, getpass, random, string
from email.mime.text import MIMEText

print('\033[32m'+'--------------------------------------------------'+'\033[0;0m')
print('        E-mail spammer!\n')
print('If you use a google email\nyou need to allow less secure app access at\n\nhttps://myaccount.google.com/u/0/security?hl=pt:')
print('\033[32m'+'--------------------------------------------------'+'\033[0;0m')

# conexão com os servidores do google
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465
# username ou email para logar no servidor
username = input('Type your e-mail: ')
password = getpass.getpass('Your password: ')

mail_from = input('Destination e-mail: ')
mail_to = [mail_from]

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))
   

amount = int(input('How many emails do you want to send: '))

i = 1

while i <= amount:
   message = MIMEText(randomword(10))
   message['subject'] = randomword(10)
   message['from'] = mail_from
   message['to'] = ', '.join(mail_to)

   # conectaremos de forma segura usando SSL
   server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)

   # fazer login nele
   try:
      server.login(username, password)
      server.sendmail(mail_from, mail_to, message.as_string())
      server.quit()
   except smtplib.SMTPAuthenticationError:
      print('\033[31m'+'Username or password invalid!'+'\033[0;0m')
      break


   i += 1
