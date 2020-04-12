# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 22:43:50 2020

@author: dasaw
"""

import cv2

photo = cv2.imread('Python.jpg')

cv2.imshow('Display Image using cv2 library', photo)
cv2.waitKey()
cv2.destroyAllWindows()