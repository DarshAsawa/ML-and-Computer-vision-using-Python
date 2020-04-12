# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 23:02:38 2020

@author: dasaw
"""


import cv2

photo = cv2.imread('Python.jpg')

print("The image dimensions are ",photo.shape)
print("Columns in this image : ",photo.shape[1])
print("Rows in this image : ",photo.shape[0])

pixel = photo.shape[2]
if pixel==3:
    print("Colorful image..")
elif pixel!=3:
    print("Black n White image or Gray Image..")
    
 #display image....   
cv2.imshow('Display Image using cv2 library', photo)
cv2.waitKey()
cv2.destroyAllWindows()