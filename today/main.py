import pafy
import cv2
import os
from matplotlib import pyplot as plt
import shutil
import numpy as np


# path = "C:\\Users\\bit\\Desktop\\new\\today\\image\\dog1.jpg"
#
# img = cv2.imread(path, cv2.IMREAD_COLOR) 읽어오기
#
# cv2.imshow('image', img)  보여주기
# cv2.waitKey(10000)    유지하기
# cv2.destroyAllWindows()   꺼주기



# 원본 파일주소
OriginImagePath = "C:\\Users\\bit\Desktop\\new\\today\\image"
# 원본사진 리스트
OriginFileList = os.listdir(OriginImagePath) # 사진 list 만들기

# 새로 저장될 장소
OutputImagePath = "C:\\Users\\bit\\Desktop\\new\\today\\output\\"

def Resize(OriginImagePath,image, num): # 사이즈 변경
    # 사진 하나하나를 읽어드립니다 컬러로
    CropImage = cv2.imread(OriginImagePath + '\\' + image, cv2.IMREAD_COLOR)

    xLength = int(input("X축 크기를 입력하세요"))
    yLength = int(input("Y축 크기를 입력하세요"))

    # cv2.resize(원본 이미지, 결과 이미지 크기, 보간법)
    ChangedImage = cv2.resize(CropImage, (xLength, yLength), cv2.INTER_AREA)

    # 자른 사진을 다른이름으로 다른 경로에 저장합니다
    cv2.imwrite(OutputImagePath + "dogs" + str(num) + ".jpg", ChangedImage)


def Rotate(OriginImagePath,image, num): # 회전(참고 : https://076923.github.io/posts/Python-opencv-6/)
    # 사진 하나하나를 읽어드립니다 컬러로
    CropImage = cv2.imread(OriginImagePath + '\\' + image, cv2.IMREAD_COLOR)

    while(1):
        angle = int(input("사진을 시계축으로 몇도 회전시키겠습니까?\n1. 90도\n2. 180\n3. 270\n"))

        if(angle == 1):
            ChangedImage = cv2.rotate(CropImage, cv2.ROTATE_90_CLOCKWISE)  # 시계방향으로 90도 회전
            break
        elif(angle == 2):
            ChangedImage = cv2.rotate(CropImage, cv2.ROTATE_180)  # 시계방향으로 180도 회전
            break
        elif (angle == 3):
            ChangedImage = cv2.rotate(CropImage, cv2.ROTATE_90_COUNTERCLOCKWISE)  # 시계방향으로 270도 회전
            break
        else:
            print("다시 입력하세요")

    # 돌린 사진을 다른이름으로 다른 경로에 저장합니다
    cv2.imwrite(OutputImagePath + "dogs" + str(num) + ".jpg", ChangedImage)



def Blur(OriginImagePath,image, num): # 모자이크
    # 사진 하나하나를 읽어드립니다 컬러로
    CropImage = cv2.imread(OriginImagePath + '\\' + image, cv2.IMREAD_COLOR)

    kernel = np.ones((2, 2), np.uint8)
    ChangedImage = cv2.filter2D(CropImage, -1, kernel)

    # Blur된 사진을 다른이름으로 다른 경로에 저장합니다
    cv2.imwrite(OutputImagePath + "dogs" + str(num) + ".jpg", ChangedImage)


def Crop(OriginImagePath,image, num): # 자르기
    
    # 사진 하나하나를 읽어드립니다 컬러로
    CropImage = cv2.imread(OriginImagePath+'\\'+image, cv2.IMREAD_COLOR)

    # 자를 부분의 x, y 좌표를 받습니다
    x1 = int(input("X축 시작점을 입력하세요"))
    x2 = int(input("X축 마지막점을 입력하세요"))
    y1 = int(input("Y축 시작점을 입력하세요"))
    y2 = int(input("Y축 마지막점을 입력하세요"))
    
    # 사진을 받은 좌표만큼 잘라서 변수에 넣어줍니다
    ChangedImage = CropImage[x1:x2, y1:y2]  # 높이를 x1 ~ x2, 가로를 y1 ~ y2

    # 자른 사진을 다른이름으로 다른 경로에 저장합니다
    cv2.imwrite(OutputImagePath+"dogs"+str(num)+".jpg", ChangedImage)


while(1):
    
    # 사용자가 어떤 메뉴를 선택할지 ui를 보여줍니다
    Choice = int(input("사진 수정파일을 실행합니다\n실행하실 항목을 선택하세요!\n1. Rsize\n2. Rotate\n3. Blur\n4. Crop\n"))
    
    # 선택한 메뉴를 들어가게끔 if문을 돌려줍니다
    if(Choice == 1):
        print("Resize을 선택하셨습니다\n")
        for num in range(0, len(OriginFileList)):  # 리스트 길이만큼 숫자 하나씩
            Resize(OriginImagePath, OriginFileList[num], num)
        print("작업을 완료하였습니다\n")
        break

    elif (Choice == 2):
        print("Rotate을 선택하셨습니다\n")
        for num in range(0, len(OriginFileList)):  # 리스트 길이만큼 숫자 하나씩
            Rotate(OriginImagePath, OriginFileList[num], num)
        print("작업을 완료하였습니다\n")
        break

    elif (Choice == 3):
        print("Blur을 선택하셨습니다\n")
        for num in range(0, len(OriginFileList)):  # 리스트 길이만큼 숫자 하나씩
            Blur(OriginImagePath, OriginFileList[num], num)
        print("작업을 완료하였습니다\n")
        break

    elif (Choice == 4):
        print("Crop을 선택하셨습니다\n")
        for num in range(0, len(OriginFileList)):  # 리스트 길이만큼 숫자 하나씩
            Crop(OriginImagePath, OriginFileList[num], num)
        print("작업을 완료하였습니다\n")
        break
                
    # 예외처리를 해줍니다
    else:
        print("\n 정확한숫자를 다시 입력해주세요!!\n")
