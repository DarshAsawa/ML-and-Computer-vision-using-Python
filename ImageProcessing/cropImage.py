# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 23:16:03 2020

@author: dasaw
"""
import cv2

photo = cv2.imread('Python.jpg')

#photo[rows_slicing,columns_slicing]
crop_photo = photo[200:290,430:750]

cv2.imshow('Display Image using cv2 library', crop_photo)
cv2.waitKey()
cv2.destroyAllWindows()