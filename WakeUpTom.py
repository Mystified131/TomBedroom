import os
from RandFunct import random_number
from RandFunct2 import random_number2
import datetime
import playsound
from PIL import Image

Imgpt = "C:\\Users\\mysti\\Coding\\TomBedroom"

contentpic = []

for subdir, dirs, files in os.walk(Imgpt):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".jpg") and "BulkImage" in str(filepath):
            contentpic.append(str(filepath))


contentaud = []

for subdir, dirs, files in os.walk(Imgpt):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".mp3") and "Generated" in str(filepath):
            contentaud.append(str(filepath))

print(contentpic)

print(contentaud)

for elem in contentaud:

    imnum = random_number(len(contentpic))

    impth = contentpic[imnum]

    image_obj = Image.open(impth)

    imnum2 = random_number(len(contentpic))

    impth2 = contentpic[imnum2]

    image_obj2 = Image.open(impth2)

    imnum3 = random_number(len(contentpic))

    impth3 = contentpic[imnum3]

    image_obj3 = Image.open(impth3)

    image_obj.show()

    playsound.playsound(elem, True)

    image_obj2.show()

    image_obj3.show()
    
## THE GHOST OF THE SHADOW ##

