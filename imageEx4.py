import cv2
import numpy as np
import os

path = "/home/ubuntu/pythonProject/data/lena.jpg"
src = cv2.imread(path)

if os.path.isfile(path):
    src = cv2.imread(path)
else:
    print("파일이 존재하지 않습니다.")

b, g, r = cv2.split(src)

height, width, channel = src.shape
print(height, width, channel)

height, width = b.shape
print(height, width)

zero = np.zeros((height, width, 1), dtype=np.uint8)
print(type(zero))
print(zero.shape)

imgB = cv2.merge((b, zero, zero))
imgG = cv2.merge((zero, g, zero))
imgR = cv2.merge((zero, zero, r))

cv2.imshow('b', imgB)
cv2.imshow('g', imgG)
cv2.imshow('r', imgR)
cv2.waitKey()
cv2.destroyWindow()