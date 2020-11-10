import os
import numpy as np
import cv2
import matplotlib.image as mpimg
import glob


from PIL import Image
# 왜곡계수를 return해주는 함수 호출
from calibration import calib, undistort
# 라인찾아주는 함수 호출
from finding_lines import Line, warp_image, find_LR_lines, draw_lane, print_road_status, print_road_map
# ???
from threshold import gradient_combine, hls_combine, comb_result

# output 폴더가 있는지 확인하고 없을시 폴더 생성
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print("output 디렉토리가 생성되었습니다")
    except OSError:
        print('Error: Creating directory. ' + directory)

createFolder('output')
# 폴더 생성 완료

# 영상저장 코덱
#fourcc = cv2.VideoWriter_fourcc(*'DIVX')
fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')



# 왜곡계수를 받아오
mtx, dist = calib()


# main 시작
left_line = Line()
right_line = Line()

th_sobelx, th_sobely, th_mag, th_dir = (35, 100), (30, 255), (30, 255), (0.7, 1.3)
th_h, th_l, th_s = (10, 100), (0, 60), (85, 255)

input_name = 'project_video.mp4'

# 비디오 읽기
cap = cv2.VideoCapture(input_name)

# 작업하고 있는 영상의 길이?크기?
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# 재생할 파일의 프레임 레이트 얻기
fps = cap.get(cv2.CAP_PROP_FPS)





num = 0
num_rm = 0

# 여기부터 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 여기부터 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 여기부터 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 여기부터 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#out1 = cv2.VideoWriter('output/combined_result_'+str(num)+'.avi', fourcc, fps, (640, 128), 0)
# out2 = cv2.VideoWriter('output/info2_'+str(num)+'.avi', fourcc, fps, (640, 360))

# 10초 카운터 생성
frameMAX = fps*10
frameCnt = 0
frameCnt2 = 0


while (cap.isOpened()):

    # 파일 용량 확인
    fileMax = 16000000  # 최대용량
    filecnt = 0

    file = os.listdir('output')
    for i in range(0, len(file)):
        if (len(file) == 0):
            break
        else:
            filestat = os.stat('output/'+str(file[i]))
            filesize = filestat.st_size
            filecnt += filesize
    print('filecnt : ' + str(filecnt))
    if (filecnt >= fileMax):
        os.remove('output/combined_result_' + str(num_rm) + '.avi')
        os.remove('output/info2_' + str(num_rm) + '.avi')
        num_rm += 1
        filecnt = 0
    else:
        filecnt = 0


    _, frame = cap.read()


    # 왜곡된 영상 펴주
    undist_img = undistort(frame, mtx, dist)

    # 영상 사이즈 줄이기
    undist_img = cv2.resize(undist_img, None, fx=1 / 2, fy=1 / 2, interpolation=cv2.INTER_AREA)
    rows, cols = undist_img.shape[:2]

    # 엣지따기
    combined_gradient = gradient_combine(undist_img, th_sobelx, th_sobely, th_mag, th_dir)


    # 컬러따기?
    combined_hls = hls_combine(undist_img, th_h, th_l, th_s)


    # 엣지 + 컬러
    combined_result = comb_result(combined_gradient, combined_hls)

    # 작업하고 있는 영상의 길이?크기?
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # 재생할 파일의 프레임 레이트 얻기
    fps = cap.get(cv2.CAP_PROP_FPS)


    ## 첫번째 저장!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # 영상 1분씩 자르기

    if (0 < frameCnt and frameCnt < frameMAX):   #계속저장
        out1.write(combined_result)
        frameCnt += 1
    elif (frameCnt == 0):
        out1 = cv2.VideoWriter('output/combined_result_' + str(num) + '.avi', fourcc, fps, (640, 128), 0)
        out1.write(combined_result)
        frameCnt += 1
    else :    # 다음단계
        frameCnt = 0


    c_rows, c_cols = combined_result.shape[:2]
    s_LTop2, s_RTop2 = [c_cols / 2 - 24, 5], [c_cols / 2 + 24, 5]
    s_LBot2, s_RBot2 = [110, c_rows], [c_cols - 110, c_rows]

    src = np.float32([s_LBot2, s_LTop2, s_RTop2, s_RBot2])
    dst = np.float32([(170, 720), (170, 0), (550, 0), (550, 720)])

    warp_img, M, Minv = warp_image(combined_result, src, dst, (720, 720))
    searching_img = find_LR_lines(warp_img, left_line, right_line)
    w_comb_result, w_color_result = draw_lane(searching_img, left_line, right_line)

    # Drawing the lines back down onto the road
    color_result = cv2.warpPerspective(w_color_result, Minv, (c_cols, c_rows))
    lane_color = np.zeros_like(undist_img)
    lane_color[220:rows - 12, 0:cols] = color_result

    # Combine the result with the original image
    result = cv2.addWeighted(undist_img, 1, lane_color, 0.3, 0)

    info, info2 = np.zeros_like(result), np.zeros_like(result)
    info[5:110, 5:190] = (255, 255, 255)
    info2[5:110, cols - 111:cols - 6] = (255, 255, 255)
    info = cv2.addWeighted(result, 1, info, 0.2, 0)
    info2 = cv2.addWeighted(info, 1, info2, 0.2, 0)

    # 왼쪽 상단 road_status 띄우기
    info2 = print_road_status(info2, left_line, right_line)

    ## 두번째 저장!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if (0 < frameCnt2 and frameCnt2 < frameMAX):  # 계속저장
        out2.write(info2)
        frameCnt2 += 1
    elif (frameCnt2 == 0):
        out2 = cv2.VideoWriter('output/info2_' + str(num) + '.avi', fourcc, fps, (640, 360))    # 칼라 조심
        out2.write(info2)
        frameCnt2 += 1
    else:  # 다음단계
        frameCnt2 = 0
        num += 1



cap.release()
out1.release()
out2.release()

print("End!!!!")





