1. Savo serverio kurimas: atsidarai CMD "python -m http.server"
2. Webe: http://127.0.0.1:8000
3. Consoleje kad uzdaryti savo serveri: ctrl + c

"""bool_list = [True, False]
print(not any(bool_list))
127.0.0.1:8000
import requests

r = requests.get("http://127.0.0.1:8000")
print(r.ok)


Parašykite funkciją, kuri į parametrus priimtų kreipinį,
el. pašto adresą ir float reikšmę ir sugeneruotų laišką,
kuriame informuotų adresatą apie susidariusį įsiskolinimą.
Laiške kur nors įterpkite logotipą."""

from os import environ
import smtplib
from email.message import EmailMessage
from string import Template

pswd = environ.get('ABC')


def apmoketi(skolininkas, el_pastas, suma):
    with open("skola.html", "r") as f:
        html = f.read()

    sablonas = Template(html)

    email = EmailMessage()
    email['from'] = 'Skolos Adminas'
    email['to'] = el_pastas
    email['subject'] = 'Pranešimas apie įsiskolinimą'

    email.set_content(sablonas.substitute(
        {'skolininkas': skolininkas,
         'suma': suma,
         'mail': el_pastas}),
        'html')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('pasitestuokime@gmail.com', pswd)
        smtp.send_message(email)

a = input("Ivesk skolininka: ")
b = input("Ivesk el pasta: ")
c = input ("Ivesk isiskolinta suma: ")
apmoketi(a, b, c)