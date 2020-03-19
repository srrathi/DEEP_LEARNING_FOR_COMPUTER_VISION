# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 14:01:49 2020

@author: Lenovo
"""

import cv2

img = cv2.imread('51702814562fa4b9b9538d7c11674630.jpg',1)

px = img[300,300]
print(px)

blue = img[:,:,0]
green = img[:,:,1]
print(blue)
print("\n\n\n\n")
print(green)
print("\n\n\n\n\n",img.shape,"\n\n\n\n",img.size)