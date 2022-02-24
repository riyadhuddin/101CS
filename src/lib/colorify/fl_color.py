# Write a function to assign random color to images in a folder
import cv2
import os
import random
from PIL import Image
from PIL import ImageColor
import requests
from io import BytesIO
url = "https://cdn.pixabay.com/photo/2017/07/26/06/34/hand-painted-2540641_1280.png"
response = requests.get(url)
img = Image.open(BytesIO(response.content))
# img.show()

img = img.convert("RGB") 
d = img.getdata()
new_image = []
for item in d:
    if item[0] < 155 and item[1] < 255 and item[2] < 255:
        new_image.append((0,0,0))
    else:
        new_image.append(item)
img.putdata(new_image)
img.show()

# write a function to assign random color to images in a folder
def random_color(img):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    img = img.convert("RGB") 
    d = img.getdata()
    new_image = []
    for item in d:
        if item[0] < 155 and item[1] < 255 and item[2] < 255:
            new_image.append((0,0,0))
        else:
            new_image.append(item)
    img.putdata(new_image)
    img.show()
    return img
# https://martechwithme.com/how-to-change-color-multiple-images-python/