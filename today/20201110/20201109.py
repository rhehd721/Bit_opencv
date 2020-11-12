import sys
import numpy as np
import cv2
import glob

srcs = glob.glob('img/chess*.jpg')



if srcs is None:
    print('Image load failed!')
    sys.exit()

for srclist in srcs:
    src = cv2.imread(srclist)
    w, h = 720, 400

    src = cv2.resize(src, dsize=(600, 600), interpolation=cv2.INTER_AREA)

    ##srcQuad = np.array([[325, 307], [760, 369], [718, 611], [231, 515]], np.float32)
    ##dstQuad = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]], np.float32)

    ##pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
    ##dst = cv2.warpPerspective(src, pers, (w, h))

    cv2.imshow('src', src)
    ##cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()