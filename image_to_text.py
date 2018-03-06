# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import cv2

import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
from PIL import Image



imgPath='C:\\Users\\adelgad6\\Desktop\\a.png';
img=Image.open(imgPath)
#print pytesseract.image_to_string(img);
'''
img = cv2.imread(imgPath,0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
