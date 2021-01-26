from cv2 import cv2
import os
import sys
from PIL import Image,ImageFilter,ImageEnhance

class Color:
    def __init__(self,filepath):
        self.filepath = filepath
    
    def gray(self):
        if os.path.exists(self.filepath) == False:
            print('Error => Invalid File Provided')
            sys.exit(1)

        else:
            img = cv2.imread(self.filepath)
            grayscaled_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            cv2.imshow('GrayScaled Image',grayscaled_img)
            cv2.waitKey()

        
    def hsv(self):
        if os.path.exists(self.filepath) == False:
            print('Error => Invalid File Provided')
            sys.exit(1)

        else:
            img = cv2.imread(self.filepath)
            hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
            cv2.imshow('HSV Image',hsv_img)
            cv2.waitKey()

            
    def rgba(self):
        if os.path.exists(self.filepath) == False:
            print('Error => Invalid File Provided')
            sys.exit(1)

        else:
            img = cv2.imread(self.filepath)
            rgba_img = cv2.cvtColor(img,cv2.COLOR_BGRA2RGBA)
            cv2.imshow('RGBAS Image',rgba_img)
            cv2.waitKey()
