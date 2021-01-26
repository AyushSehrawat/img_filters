from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import sys
from PIL import Image,ImageFilter,ImageEnhance

class Filter:
    def __init__(self,filepath):
        self.filepath = filepath

    def blur(self,p1,p2):
        try:
            if os.path.exists(self.filepath) == False:
                print('Error => Invalid File Provided')
                sys.exit(1)
            else:
                image = cv2.imread(self.filepath)
                ksize = (p1, p2)
                image = cv2.blur(image, ksize)
                cv2.imshow('Blur', image)
                cv2.waitKey()
        except ValueError:
            print('Error => Value Error')


    
    def edge(self):
        if os.path.exists(self.filepath) == False:
            print('Error => Invalid File Provided')
            sys.exit(1)
        else:
            img = cv2.imread(self.filepath,0)
            edges = cv2.Canny(img,100,200)
            plt.subplot(121),plt.imshow(img,cmap = 'gray')
            plt.title('Original Image'), plt.xticks([]), plt.yticks([])
            plt.subplot(122),plt.imshow(edges,cmap = 'gray')
            plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

            plt.show()

    
    def contrast(self,val):
        try:
            val = float(val)

            if os.path.exists(self.filepath) == False:
                print('Error => Invaid File Provided')
                sys.exit(1)
            else:
                im = Image.open(self.filepath)
                enh = ImageEnhance.Contrast(im)
                enh.enhance(val).show('Contrast')
        except ValueError:
            print('Error => ValueError')

        
    def sharp(self,val):
        try:
            val = float(val)

            if os.path.exists(self.filepath) == False:
                print('Error => Invaid File Provided')
                sys.exit(1)
            else:
                im = Image.open(self.filepath)
                enh = ImageEnhance.Sharpness(im)
                enh.enhance(val).show('Sharpness')
        except ValueError:
            print('Error => ValueError')

            
    def imgcolor(self,val):
        try:
            val = float(val)

            if os.path.exists(self.filepath) == False:
                print('Error => Invaid File Provided')
                sys.exit(1)
            else:
                im = Image.open(self.filepath)
                enh = ImageEnhance.Color(im)
                enh.enhance(val).show('Image Color Balance')
        except ValueError:
            print('Error => ValueError')

                
    def bright(self,val):
        try:
            val = float(val)

            if os.path.exists(self.filepath) == False:
                print('Error => Invaid File Provided')
                sys.exit(1)
            else:
                im = Image.open(self.filepath)
                enh = ImageEnhance.Brightness(im)
                enh.enhance(val).show('Brightness')
        except ValueError:
            print('Error => ValueError')
