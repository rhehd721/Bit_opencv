import cv2
import os

path = "/home/ubuntu/pythonProject/data/lena.jpg"

src = cv2.imread(path)
size = (256, 256)

dst = cv2.resize(src, dsize=size, interpolation=cv2.INTER_LINEAR)
dst2 = cv2.resize(src, dsize=(0, 0), fx=0.8, fy=0.8, interpolation=cv2.INTER_LINEAR)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()


