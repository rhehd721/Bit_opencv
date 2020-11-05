import pafy
import cv2

url = 'https://www.youtube.com/watch?v=SmbWkZdH7OI'
video = pafy.new(url)

print(video.title) # 제목
print(video.rating) # 평점
print(video.viewcount) # 조회수
print(video.author) # 저작권자
print(video.length) # 125sec
print(video.duration) #
print(video.likes) #
print(video.dislikes) #

best = video.getbest(preftype="mp4") # 3gp
print(best.resolution)

cap = cv2.VideoCapture(best.url)

### 비디오 파일 저장
framewidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frameRate = int(cap.get(cv2.CAP_PROP_FPS))
print(frameRate)

breakKey = 99  # 아스키코드 참고 "c == 99"

frame_size = (framewidth, frameHeight)

# codec 및 녹화 관련 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# fourcc = cv2.VideoWriter_fourcc(*'MPEG')
# fourcc = cv2.VideoWriter_fourcc(*'X264')


out1path = "/home/ubuntu/pythonProject/data/recod1.mp4"
out2path = "/home/ubuntu/pythonProject/data/recod2.mp4"
out1 = cv2.VideoWriter(out1path, fourcc, frameRate, frame_size)
# out2 = cv2.VideoWriter(out2path, fourcc, frameRate, frame_size)

frameCount = 0

# 동영상 프레임 캡쳐
while True:
    # 한장의 이미지를 가져온다
    # 이미지 -> frame
    # 정상적으로 읽어왔는지 -> retval
    retval, frame = cap.read()
    if not (retval) or frameCount == 290:
        break  # 프레임정보를 정상적으로 읽지 못하면 while 문을 빠져나온다

    # 여기서부터 엣지 따오기 주석처리하면 컬러출력
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    # 엣지 종료

    # 동영상 파일에 쓰기
    out1.write(frame)
    # out2.write(edges)

    frameCount += 1



    # 파일출력
    cv2.imshow('frame', frame)
    cv2.imshow('edges', edges)

    key = cv2.waitKey(frameRate)  # 33 msec 동안 힌 프레임을 보여준다 (초당 30frame)

    # 키 입력을 받으면 키값을 key로 저장    'esc == 27'
    if key == 27:
        break
    if key == breakKey:
        break

if cap.isOpened():
    cap.release()

out1.release()
cv2.destroyAllWindows()