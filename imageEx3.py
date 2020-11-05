import cv2
import os

path = "/home/ubuntu/pythonProject/data/lena.jpg"
src = cv2.imread(path)

if os.path.isfile(path):
    gray = cv2.imread(path, 0)
else:
    print("파일이 존재하지 않습니다.")

# 채널별로 이미지를 분리

imgRGB = cv2.merge((gray, gray, gray))

cv2.imshow('gray', gray)
cv2.imshow('imgRGB', imgRGB)

cv2.waitKey()
cv2.destroyWindows()
