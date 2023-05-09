#!python

import qrcode
import os
import sys

link = sys.argv[1]
def qr_generator(link:str):
    
    img = qrcode.make(link)
    name = input('Enter the name you want to save the image to : ')
    
    os.chdir(os.path.dirname(__file__))
    
    if name.endswith('.png'):
        img.save(name)
    else:
        img.save(name + '.png')
    
    print("Image been saved !!")
    
qr_generator(link)
