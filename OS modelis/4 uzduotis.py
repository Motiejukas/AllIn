"""Sukurti minibiudžeto programą, kuri:

Leistų vartotojui įvesti pajamas arba išlaidas (su "-" ženklu)
Pajamas ir išlaidas saugotų sąraše, o sąrašą pickle faile (uždarius programą, įvesti duomenys nedingtų)
Atvaizduotų jau įvestas pajamas ir išlaidas
Atvaizduotų įvestų pajamų ir išlaidų balansą (sudėtų visas pajamas ir išlaidas)
Patarimas:

import pickle
"""
import pickle

while True:
    try:
        with open("biudzetas.pkl", "rb") as pickle_in:
            biudzetas = pickle.load(pickle_in)
            suma = 0
            print("--------Įrašų sąrašas:---------")
            for skaicius, irasas in enumerate(biudzetas):
                suma += irasas
                print(skaicius + 1, irasas)
            print("Biudžeto balansas", suma)
            print("-------------------------------")
    except:
        print("Nepavyko nuskaityti failo")
        biudzetas = []
    print("Norėdami išeiti palikite tuščią lauką ir spauskite ENTER")
    irasas = float(input("Įveskite pajamas arba išlaidas: "))
    if irasas == "":
        break
    biudzetas.append(irasas)

    try:
        with open("biudzetas.pkl", "wb") as pickle_out:
            pickle.dump(biudzetas, pickle_out)
    except:
        print("Nepavyko įrašyti failo")