import random
import os
import datetime
from RandFunct import random_number
from RandFunct2 import random_number2
from subprocess import call
import cv2
import numpy as np
from PIL import Image

def crop(image_path, coords, saved_location):
    image_obj = Image.open(image_path)
    #image_obj.show()
    cropped_image = image_obj.crop(coords)
    #cropped_image.show()
    cropped_image.save(saved_location)

#Imgpt = "F:\\Visual\\VisualArt"

#Imgpt = "C:\\Users\\mysti\\Desktop\\TomBedroom"

Imgpt = "C:\\Users\\mysti\\Desktop\\TomBedroomElements\\screenshots"

contentgraph = []

for subdir, dirs, files in os.walk(Imgpt):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".png"):
            contentgraph.append(str(filepath))

print(contentgraph)

plen = len(contentgraph)

for ctr in range(plen):

    elm = contentgraph[ctr]

    nelm = str(ctr) + "_CROP.png"

    print(nelm)

    crop(elm, (300, 55, 1470, 760), nelm)

Imgpt = "C:\\Users\\mysti\\Coding\\TomsBedroom"

contentgraph2 = []

for subdir, dirs, files in os.walk(Imgpt):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".png") and "CROP" in str(filepath):
            contentgraph2.append(str(filepath))

plen = len(contentgraph2)

print(contentgraph2)

for ctr in range(3):

    right_now = datetime.datetime.now().isoformat()
    list = []

    for i in right_now:
        if i.isnumeric():
            list.append(i)

    tim = ("".join(list))

    a = random_number2(50, 232)
    b = random_number2(50, 232)
    c = random_number2(50, 232)

    for cotr in range(plen):

        print("")

        print("Generating Art: " + (str(ctr + cotr)))
            
        ppt = contentgraph2[cotr]

        print(ppt)

        m =  cv2.imread(ppt)

        h,w,bpp = np.shape(m)

        bi = np.zeros((h,w,3), np.uint8)

        try: 
            
            for py in range(0,h):
                for px in range(0,w):
            #can change the below logic of rgb according to requirements. In this 
            #white background is changed to #e8e8e8  corresponding to 232,232,232 
            #intensity, red color of the image is retained.
                    #f(m[py][px][0] >200): 
                        
                    bi[py][px][0] =  m[py][px][0] + a
                    bi[py][px][1] =  m[py][px][1] + b
                    bi[py][px][2] =  m[py][px][2] + c

                
            outpath =  "C:\\Users\\mysti\\Coding\\Fractalizer\\BulkImage" + str(tim) + str(ctr + cotr) +".jpg"
            

            #cv2.imshow('matrix', bi)
            #cv2.waitKey(0)
            cv2.imwrite(outpath, bi)

        except:
            print("")
            print("Process error.")
            print("")

print("")

print("Images created and saved in the output folder.")

print("")

#call(["python", "BatchDeleter.py"])

## THE GHOST OF THE SHADOW ##
