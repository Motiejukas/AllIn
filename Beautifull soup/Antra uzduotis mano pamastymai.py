"""Parašykite žaidimą, kuris iš svetainės http://quotes.toscrape.com/ pateiks citatas, o žaidėjui reikės atspėti autorių.
Žaidėjui neatspejus, reikės pasufleruoti autoriaus inicialus, dar kartą neatspėjus - gimimo datą ir vietą. Jeigu žaidėjas
neatspėja iš 3 kartų, jam atspausdinamas teisingas atsakymas ir paklausiama, ar nori tęsti."""

import requests
from bs4 import BeautifulSoup
from random import shuffle
from random import randint

html = requests.get('http://quotes.toscrape.com/').text
soup = BeautifulSoup(html, "html.parser")

citatu_tagai = soup.select('.text')
citatos = [i.get_text() for i in citatu_tagai]

a_blocks = soup.find_all('a', attrs={'class': None})
hrefs = [i['href'] for i in a_blocks if i.get_text()=="(about)"]
print(hrefs)

autoriu_tagai = soup.select('.author')
autoriai = [i.get_text() for i in autoriu_tagai]




while True:
    break