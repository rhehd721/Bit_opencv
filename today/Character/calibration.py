import numpy as np
import cv2
import matplotlib.image as mpimg
import glob

# 특정 카메라로 찍은 체스판 이미지들을 불러온다
images = glob.glob('chessImages/chess*.jpg')


# 이미지에서 추출해낸 값들을 저장할 list함수
objpoints = []
imgpoints = []

def calib():

    # 내가 사용한 체스판의 특징을 입력해준다
    objp = np.zeros((7 * 9, 3), np.float32)
    objp[:, :2] = np.mgrid[0:9, 0:7].T.reshape(-1, 2)  # x,y coordinates

    # 이미지 하나하나 불러오기
    for fname in images:

        # 이미지 하나하나 읽기
        img = mpimg.imread(fname)
        # 이미지를 BGR에서 GRAY로 변경
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 이미지에서 모서리와 ret 추출하기
        ret, corners = cv2.findChessboardCorners(gray, (9, 7), None)

        # If corners are found, add object points, image points
        if ret == True:
            imgpoints.append(corners)
            objpoints.append(objp)
        else:
            continue

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    # 왜곡계수를 반환한다
    return mtx, dist

# 이미지와 왜곡계수를 넣으면 수정된 이미지를 만들어준다
def undistort(img, mtx, dist):
    """ undistort image """
    return cv2.undistort(img, mtx, dist, None, mtx)