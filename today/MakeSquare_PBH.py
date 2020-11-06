# 0311.py
import numpy as np
import cv2

# 좌표값 + 가로세로 크기

def onMouse(event, x, y, flags, param):
    global pt1

    # 버튼을 눌렀을 때
    if event == cv2.EVENT_LBUTTONDOWN:
        pt1 = (x,y)

    # 버튼 땠을 때
    if event == cv2.EVENT_LBUTTONUP:
        pt2 = (x,y)
        cv2.rectangle(param[0], pt1, pt2, (255, 255, 0), 2)  # 2는 선 두께

        org = [0,0]
        if(pt1[0] > pt2[0]):
            org[0] = pt2[0]
            xLength = pt1[0] - pt2[0]
        elif (pt1[0] < pt2[0]):
            org[0] = pt1[0]
            xLength = pt2[0] - pt1[0]

        if (pt1[1] > pt2[1]):
            org[1] = pt2[1]
            yLength = pt1[1] - pt2[1]
        elif (pt1[1] < pt2[1]):
            org[1] = pt1[1]
            yLength = pt2[1] - pt1[1]

        text = 'X : '+str(pt1)+' Y : '+str(pt2)+' xLength' +str(xLength) +' yLength' + str(yLength)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(param[0], text, tuple(org), font, 0.3, (255, 0, 0), 1)

    # 더블클릭
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        param[0] = np.zeros(param[0].shape, np.uint8) + 255
    cv2.imshow("img", param[0])


img = np.zeros((512, 512, 3), np.uint8) + 255   # 백지만들기
cv2.imshow('img', img)  # 백지창 띄우기

cv2.setMouseCallback('img', onMouse, [img])

cv2.waitKey()
cv2.destroyAllWindows()
