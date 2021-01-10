

"""from PIL import Image, ImageEnhance

def sugeneruoti(pic, R, G, B):
    nuotrauka = Image.open(pic)
    pikseliai = nuotrauka.getdata()
    balti_pikseliai = 255, 255, 255
    juodi_pikseliai = 0, 0, 0
    nauji_duomenys = []
    for piks in pikseliai:
        if piks[0] >= R or piks[1] >= G or piks[2] >= B:
            nauji_duomenys.append(juodi_pikseliai)
        else:
            nauji_duomenys.append(balti_pikseliai)

    nuotrauka.putdata(nauji_duomenys)
    return nuotrauka

nuotraukite = sugeneruoti('suo.png', 234, 100, 100)
nuotraukite.show()

"""
