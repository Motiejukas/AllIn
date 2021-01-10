import os



with open("failas.py", 'r', encoding="utf-8") as failas1:
    def bbz():
        skaitau_faila = failas1.read()
        iskirta = skaitau_faila.split()
        for i in iskirta:
            if i != "=":
                return i

print(bbz())

"""listas = "Čia yra pirmas failo sakinys"
def funkcija_cbb():
    iskyrimas = listas.split()
    return f"{iskyrimas[0]}{iskyrimas[1]}{iskyrimas[2]}{iskyrimas[3]}{len(iskyrimas)}"
print(funkcija_cbb())"""