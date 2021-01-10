"""127.0.0.1:8000
import requests

r = requests.get("http://127.0.0.1:8000")
print(r.ok)"""

from os import environ
import smtplib
from email.message import EmailMessage
from string import Template

pswd = environ.get('ABC')

def apmoketi(skolininkas, el_pastas, suma):



# elementarios email žinutės sukūrimas:
email = EmailMessage()
email['from'] = 'Vardas Pavardė'
email['to'] = 'adresatas@gmail.com'
email['subject'] = 'email from python'

email.set_content('Sveiki adresate,\n\nČia yra laiško turinys\n\npagarbiai, siuntėjas')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('pasitestuokime@gmail.com', pswd)
    smtp.send_message(email) # išsiunčiame žinutę

