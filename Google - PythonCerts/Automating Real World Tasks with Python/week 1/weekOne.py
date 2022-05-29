from PIL import Image
import os

img_list = [i for i in os.listdir() if i.startswith('ic_')]

for i in img_list:
    img = Image.open(i)
    # rotate to rotate the file and resize to resize in the resolution given 
    # and convert to convert the file in RGB(else gives error) and save to
    #  save in the format JPEG
    img.rotate(-90).resize((128, 128)).convert('RGB').save(f"/opt/icons/{i}", "JPEG")
