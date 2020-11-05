# 파이썬에서 openCV를 사용하기 위해
import cv2
# matplotlib 패키지에서 pyplot를 plt 라는 이름으로 임포트 한다.
from matplotlib import pyplot as plt

import os

print(os.path.isfile("./data/lena.jpg")) # 파일 있는지 확인하기

# 파일이 저장된 경로를 문자열 객체 지정
imageFile = './data/lena.jpg'

# BGR포맷으로 읽어서 img 객체에 저장한다.
imgBGR = cv2.imread(imageFile)  # cv2.IMREAD_COLOR

# X, Y축을 표시하지 않는다.
plt.axis('off')
# plt.imshow(imgBGR)
# plt.show()

# plot에 그리기 위해서는 RGB순서의 포맷이어야 한다.
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
plt.imshow(imgRGB)  # plot에 imgRGB를 그리고
plt.show()  # plot에 그린 내용을 출력한다.

# import cv2
#
# imageFile = './data/lena.jpg'
# #
# img = cv2.imread(imageFile)
#
# # cv2.imwrite('./data/lena.bmp', img)
# #
# # cv2.imwrite('./data/lena.png', img)
# #
# # cv2.imwrite('/data/lena2.png',img,[cv2.IMWRITE_PNG_COMPRESSION,9])
# #
# # cv2.imwrite('/data/lena2.jpg',img,[cv2.IMWRITE_JPEG_QUALITY,90])
#
# imageFile = './data/lena2.jpg'
#
# img2 = cv2.imread(imageFile,0)
#
#
#
# # cv2.imshow('Lena color', img)
#
# cv2.imshow('Lena grayscale', img2)
#
# cv2.waitKey()
# cv2.destroyWindow()

