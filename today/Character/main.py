# 글자인식 프로그램 만들기 Character_recognition
# 1. 사진 펴주기
# 2. 종이부분 따오기
# 3. 글자인식하기
import numpy as np
import cv2
import matplotlib.image as mpimg
import glob
import os

from calibration import calib, undistort

########## 사진을 펴주고 result를 저장할 공간 생성하기 ##########
# 내가 읽고자 하는 글자 사진
originalImage = 'inPut/'

# 왜곡계수 받아오기
mtx, dist = calib()

# 내가 사용할 사진 펴주기
modifiedImage = undistort(originalImage, mtx, dist)

# output 폴더가 있는지 확인하고 없을시 폴더 생성
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print("outPut 디렉토리가 생성되었습니다")
    except OSError:
        print('Error: Creating directory. ' + directory)

createFolder('outPut')
# 폴더 생성 완료

########## 글자인식부분 만들기 ##########

