#!python



import os
import sys
try:
    import qrcode
except:
    os.system("pip install qrcode")

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
