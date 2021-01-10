"""sukurkite funkciją, kuri priimtų

paveikslėlį
kontrasto, spalvingumo, aštrumo ir ryškumo reikšmes
išsaugoti ar ne reikšmę
ir atitinkamai pakoreguotų paveikslėlio nustatymus.
Parodytų nuotrauką ekrane. Priklausomai nuo pasirinkimo,
išsaugotų arba ne. Išsaugokite faile, prie originalaus pavadinimo
pridėję pvz. '_modified', tarkime dog_modified.jpg."""

from PIL import Image, ImageEnhance
import os

def enhance_image(pic, contrast, color, sharpness, brightness, save=False):
    im = Image.open(pic)
    enh = ImageEnhance.Contrast(im)
    im = enh.enhance(contrast)
    enh = ImageEnhance.Color(im)
    im = enh.enhance(color)
    enh = ImageEnhance.Brightness(im)
    im = enh.enhance(brightness)
    enh = ImageEnhance.Sharpness(im)
    im = enh.enhance(sharpness)
    if save:
        loc = os.path.splitext(pic)[0]
        ext = os.path.splitext(pic)[1]
        im.save(f'{loc}_modified{ext}')
    im.show()

enhance_image('dog.jpg', 2, 0, 5, 1, True)