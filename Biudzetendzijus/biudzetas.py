"""Turi būti sukurtos klasės: Biudzetas, PajamuIrasas, IslaiduIrasas, failas main"""


class Biudzetas():
    pradine_suma = 0
    pajamos1 = []
    islaidos1 = []

    def ivesti_pajamas(self, suma):
        pajamos = Irasas("Pajamos", suma)
        self.zurnalas.append(pajamos)



    def ivesti_islaidas(self):
        pass




class Irasas():

    def pajamos(self):
        pass


    def islaidos(self):
        pass



biudzetas = Biudzetas()
irasas = Irasas()


while True:
    pasirinkimas = int(input(f" 1 - Iveskit pajamas \n 2 - Iveskite islaidas \n 3 - Jusu balansas\n 4 - Ataskaita\n 0 - Iseiti\n\tJusu pasirinkimas: "))
    if pasirinkimas == 1:
        suma = str(input("Įveskite pajamų sumą: "))
        biudzetas.ivesti_pajamas()
    if pasirinkimas == 2:
        pass
    if pasirinkimas == 3:
        pass
    if pasirinkimas == 4:
        pass
    if pasirinkimas == 0:
        pass
