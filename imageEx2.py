import cv2
import os

path = "/home/ubuntu/pythonProject/data/lena.jpg"
src = cv2.imread(path)

if os.path.isfile(path):
    src = cv2.imread(path)
else:
    print("파일이 존재하지 않습니다.")

# 채널별로 이미지를 분리

b, g, r = cv2.split(src)
imgRGB = cv2.merge((r, g, b))


cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)
cv2.imshow('imgRGB', imgRGB)

cv2.waitKey()
cv2.destroyWindows()