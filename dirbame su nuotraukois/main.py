from PIL import Image, ImageEnhance

"""Turime logo su peršviečiamu fonu,
dydis 128*128. Atsisiųskite, ir perdarykite taip, 
kad nuo viršaus ir apačios nusiimtų po 28 eilutes pikselių. 
Išsisaugokite, nes naudosime sekančioms užduotims."""

"""logo = Image.open("logo.png")
print(logo.size, logo.mode)
box = (0, 28, 128, 100)
lol_apkarp = region = logo.crop(box)


lol_apkarp.save("apkarpytas_logo.png")
logo1 = Image.open("apkarpytas_logo.png")
print(logo1.size, logo1.mode)"""

paveikslelis = "suo.png"

def kon(kontrastas):
    suo = Image.open(paveikslelis)
    enh = ImageEnhance.Contrast(suo)
    enh.enhance(kontrastas).show()
    if input("Ar issaugoti nuotrauka (yes or no)") == "yes":
        enh.enhance(kontrastas).save("kontrastuotas pudeliukas.png")
    else:
        print("vali nx")

def spalv(spalvingumas):
    suo = Image.open(paveikslelis)
    enh1 = ImageEnhance.Color(suo)
    enh1.enhance(spalvingumas).show()
    if input("Ar issaugoti nuotrauka (yes or no)") == "yes":
        enh1.enhance(spalvingumas).save('spalvingas sunekas.png')
    else:
        print("vali nx")



print(kon(0.1))



