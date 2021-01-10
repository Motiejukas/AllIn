"""Parašykite programą, kuri nuskaitytų delfi antraštes, patikrintų, ar jos turi dvitaškį.
Dalį iki dvitaškio sudėtų į vieną sarašą, dalį po dvitaškio į kitą. Antrą sarašą išmaišykite
(google). Tuomet atspausdinkite pirmas dalis iš pirmo sarašo, prie jų prijunkite antras dalis iš
antro sąrašo. Turėtume gauti panašių variantų:

Orai : už 9 šlakius teks sumokėti 26 tūkstančius eurų
Antradienio vakare kauniečius išgąsdino termofikacijos elektrinė : ar bus naujagimių bumas?
Sukurkite blogų žodžių sąrašą, pagal kurį išsifiltruoja pranešimai apie COVID, mirtis ir t.t. Išfiltruokite ankstyvoje stadijoje, kol dar antraštės neperskirtos"""


import requests
from bs4 import BeautifulSoup
from random import shuffle

visos_antrastes = []

r = requests.get('http://delfi.lt')
tekstas = r.text
html = tekstas
soup = BeautifulSoup(html, "html.parser")

antrastes = soup.find_all(class_='CBarticleTitle')
for antraste in antrastes:
    a = antraste.get_text()
    visos_antrastes.append(a)


iki_dvitaskio = []
po_dvitaskio = []
for visos in visos_antrastes:
     if ':' in visos:
        splitted = visos.split(":")
        iki_dvitaskio.append(splitted[0])
        po_dvitaskio.append(splitted[1])

shuffle(po_dvitaskio)

for i in range(len(iki_dvitaskio)):
    print(iki_dvitaskio[i], ":", po_dvitaskio[i])


"""pattern = re.compile(r':')
res = pattern.findall(visos_antrastes)
print(res)"""
