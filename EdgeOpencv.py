import sys

import cv2
import numpy as numpy

#we need to load the image - in my case 'me.jpg'
#convert it to grayscale

input_file = sys.argv[1]
img = cv2.imread(input_file,cv2.IMREAD_GRAYSCALE)
h,w = img.shape

sobel_horizontal = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel_vertical = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
laplacian = cv2.Laplacian(img, cv2.CV_64F)
canny= cv2.Canny(img, 50, 240)

cv2.imshow('Original',img)
cv2.imshow('Sobel Horizontal',sobel_horizontal)
cv2.imshow('Sobel Vertical',sobel_vertical)
cv2.imshow('Laplacian',laplacian)
cv2.imshow('canny',canny)

cv2.waitKey()