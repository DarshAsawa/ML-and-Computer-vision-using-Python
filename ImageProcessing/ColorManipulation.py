# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 23:36:54 2020

@author: dasaw
"""


import cv2
import numpy as np
photo = cv2.imread('Python.jpg')

#In use of cv2 library - RGB(Red,Green,Blue) values are ordered in BGR format..... 
B,G,R = cv2.split(photo)

#using numpy to create a zeros array..
zero = np.zeros((404,814))
z = zero.astype('uint8')

#Creating a new image consisting no Red color...
new_photo = cv2.merge([B,G,z])

cv2.imshow('Display Image using cv2 library', new_photo)
cv2.waitKey()
cv2.destroyAllWindows()