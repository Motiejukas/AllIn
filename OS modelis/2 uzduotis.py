"""Sukurti programą, kuri:

Leistų vartotojui įvesti norimą eilučių kiekį
Įrašytų įvestą tekstą atskiromis eilutėmis į failą
Leistų vartotojui įrašyti norimą kuriamo failo pavadinimą
Patarimai:

Sukurti while ciklą, kuris užsibaigtų tik įvedus vartotojui tuščią eilutę (nuspaudus ENTER)"""
from datetime import datetime

pirmas = "Netuščias"
tekstas = ""

while pirmas != "":
    pirmas = input("Įveskite eilutę: ")
    if pirmas != "":
        tekstas += pirmas + "\n"
    else:
        break

failo_pavadinimas = input("Įveskite failo pavadinimą: ")

with open(failo_pavadinimas + ".txt", "w", encoding="UTF-8") as failas:
    failas.write(tekstas)