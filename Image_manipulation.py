#!/usr/bin/env python3
import os
from PIL import Image

image_dir = os.path.join(os.environ['HOME'],'images')
image_names = [fn for fn in os.listdir(image_dir) if fn != ('.DS_Store')]

#print(os.environ['HOME'])
#print(os.path.dirname(__file__))

def image_change():
    for image in image_names:
        file_name, file_extention = os.path.splitext(image)
        im = Image.open(os.path.join(image_dir,image))
        im = im.resize((128,128))
        im = im.convert("RGB")
        im = im.rotate(90)
        im.save(os.path.join("/opt/icons/",file_name)+".jpeg","JPEG")

image_change()
