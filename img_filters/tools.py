from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import sys
from PIL import Image,ImageFilter,ImageEnhance

class Tools:
    def __init__(self,filepath):
        self.filepath = filepath

    def rotate(self,angle):
        try: 
            angle = int(angle)
            img = Image.open(self.filepath)  
            img = img.rotate(angle)  
            img.show("Rotated Image")
            print('Errors => IO Error')

        except ValueError:
            print('Error => ValueError | Only input int type')

    
        
    def flip(self):
        if os.path.exists(self.filepath) == False:
            print('Error => Invalid File Provided')
            sys.exit(1)
        else:
            img = cv2.imread(self.filepath)
            image = cv2.flip(img, 0)
            cv2.imshow('Flip', image) 
            cv2.waitKey()