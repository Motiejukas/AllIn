"""Sukurkite programą, kuri, gavusi nuorodą į katalogą, praiteruos visus jame esančius
failus, išrinks nuotraukas, pakeis dydį pagal jūsų nurodytą aukštį išlaikant proporcijas,
 ir kiekvienos nuotraukos apatiniame dešiniajame kampe įdės logotipą, tą kurį išsisaugojote
  pirmoje užduotyje. Naudokite .resize, kadangi nuotrauką galbūt reikės padidinti, nebūtinai
  tik sumažinti."""

from PIL import Image
import os

def get_list(folder):
    files = os.listdir(folder)
    images = []
    for i in files:
        if i.endswith(('.jpg', '.png')):
           images.append(folder+'/'+i)
    return images

def pic_resize(pic, height):
    im = Image.open(pic)
    width = round(im.size[1]/im.size[0]*height)
    im = im.resize((height, width))
    return im

def optimize_images(folder, height):
    os.mkdir(f'{folder}/optimized')
    logo = Image.open('logo_cropped.png')
    pic_num = 0
    for i in get_list(folder):
        pic = Image.open(i)
        pic = pic_resize(i, height)
        logo_location = (
            pic.size[0]-logo.size[0],
            pic.size[1]-logo.size[1],
            pic.size[0],
            pic.size[1])
        pic.paste(logo, logo_location, logo)
        pic_num += 1
        pic.save(f'{folder}/optimized/picture_{pic_num}.png')