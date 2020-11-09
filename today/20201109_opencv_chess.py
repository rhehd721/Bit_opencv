import numpy as np
import cv2
import matplotlib.image as mpimg
import glob
import os

# Read in and make a list of calibration images
images = glob.glob('img/chess*.jpg')

# img = os.listdir('img')

# Array to store object points and image points from all the images

objpoints = []  # 3D points in real world space
imgpoints = []  # 2D points in image plane

def calib():
    # Prepare object points

    # 가로7 세로9 3개??
    objp = np.zeros((7 * 9, 3), np.float32)

    # np.mgrid[0:9, 0:7]
    # np.mgrid[0:5, 0:5]
    # array([[[0, 0, 0, 0, 0],
    #         [1, 1, 1, 1, 1],
    #         [2, 2, 2, 2, 2],
    #         [3, 3, 3, 3, 3],
    #         [4, 4, 4, 4, 4]],
    #        [[0, 1, 2, 3, 4],
    #         [0, 1, 2, 3, 4],
    #         [0, 1, 2, 3, 4],
    #         [0, 1, 2, 3, 4],
    #         [0, 1, 2, 3, 4]]])
    objp[:, :2] = np.mgrid[0:9, 0:7].T.reshape(-1, 2)  # x,y coordinates

    for fname in images:
        print("ing")
        print(fname)

        # 이미지 읽어오기
        img = mpimg.imread(fname)

        img = cv2.resize(img, None, fx=1 / 2, fy=1 / 2, interpolation=cv2.INTER_AREA)

        # gray로 전환
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 그림에서 체스판 모서리 찾아주기
        ret, corners = cv2.findChessboardCorners(gray, (9, 7), None)

        # If corners are found, add object points, image points
        if ret == True:
            # 모서리 넣어주기
            imgpoints.append(corners)
            # ??
            objpoints.append(objp)
        else:
            continue

    # 왜곡계수 구하기
    # ret, mtx, dist = 왜곡, rvecs = none, tvecs = none
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)


    return mtx, dist

def undistort(img, mtx, dist):
    """ undistort image """
    return cv2.undistort(img, mtx, dist, None, mtx)


mtx, dist = calib()

print(images)

for i in images:

    img = cv2.imread(i)

    undist_img = undistort(img, mtx, dist)
    undist_img = cv2.resize(undist_img, None, fx=1 / 2, fy=1 / 2, interpolation=cv2.INTER_AREA)

    # Combine the result with the original image
    cv2.imshow('result', undist_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

