# 1. 내가 이용하는 지하철 역(승차역, 하차역)의 정보를 골라서 데이터프레임으로 저장
# 2. 1번의 데이터에서 1월의 데이터만 선택
# 3. 승차역과 하차역에서 가장 이용객이 적은 시간은?

# 4. 2번의 데이터에서 월별 통계 데이터를 확인 (7~9시 사이의 승차역과 하차역의 평균치) 어느 요일이 이용객이 가장 많고 적은가?
# 5. 1~12월까지중 이용객이 가장 많은달은? (7~9시 사이)

import pandas as pd
import datetime

times = ['06시 이전', '06 ~ 07', '07 ~ 08', '08 ~ 09', '09 ~ 10', '10 ~ 11',
         '11 ~ 12', '12 ~ 13', '13 ~ 14', '14 ~ 15', '15 ~ 16', '16 ~ 17',
         '17 ~ 18', '18 ~ 19', '19 ~ 20', '20 ~ 21', '21 ~ 22', '22 ~ 23', '23 ~ 24', '24시 이후']

month = ['2019-02-01', '2019-03-01', '2019-04-01', '2019-05-01',
         '2019-06-01', '2019-07-01', '2019-08-01', '2019-09-01', '2019-10-01',
         '2019-11-01', '2019-12-01', '2020-01-01', ]

week = ['월', '화', '수', '목', '금', '토', '일']

########################################################### 내가 쓸부분 구하기 ##########################################
# 내가 사용할 데이터파일 불러오기
df = pd.read_excel('subway.xlsx')

# 강남과 신도림데이터 추출
GangnamData = df[df['역명'] == '강남']
SindorimData = df[df['역명'] == '신도림']

# 강남과 신도림으로 나눈 데이터 저장
GangnamData.to_excel(excel_writer = 'data/GangnamData.xlsx')
SindorimData.to_excel(excel_writer = 'data/SindorimData.xlsx')

# 1월 데이터만 추출
df = GangnamData[ GangnamData['날짜'] < pd.to_datetime('2019-02-01')]
df.to_excel(excel_writer='data/GangnamJanuary.xlsx')
df = SindorimData[ SindorimData['날짜'] < pd.to_datetime('2019-02-01')]
df.to_excel(excel_writer='data/SindorimJanuary.xlsx')
######################################################## 내가 쓸부분 구하기 END##########################################

# 저장한 데이터 읽어오기
GangnamJanuary = pd.read_excel('data/GangnamJanuary.xlsx')
SindorimJanuary = pd.read_excel('data/SindorimJanuary.xlsx')

############################################################## 최소시간 구하기 ##########################################
# 강남 바구니 만들기
GangnamRideList = []    # 시간대별 최소값을 담을 딕셔너리
GangnamQuitList = []    # 시간대별 최소값을 담을 딕셔너리
GangnamRideDic = {}    # 시간대별 최소값을 담을 딕셔너리
GangnamQuitDic = {}    # 시간대별 최소값을 담을 딕셔너리

# 승차와 하차 구별하기
GangnamRide = GangnamJanuary[GangnamJanuary['구분'] == '승차']
GangnamQuit = GangnamJanuary[GangnamJanuary['구분'] == '하차']

# 시간별 이용자 평균값 넣어주기
for time in times:
    GangnamRideDic[GangnamRide[time].mean()] = time
    GangnamQuitDic[GangnamQuit[time].mean()] = time
    GangnamRideList.append(GangnamRide[time].mean())
    GangnamQuitList.append(GangnamQuit[time].mean())

# 최소이용률 구하기
GangnamRideList.sort()
GangnamQuitList.sort()

# 이용객이 가장 적은 시간대 print
print("강남역에서 승차가 제일 적은 시간은 : ", GangnamRideDic[GangnamRideList[0]])
print("강남역에서 하차가 제일 적은 시간은 : ", GangnamQuitDic[GangnamQuitList[0]])

# 신도림 바구니 만들기
SindorimRideList = []    # 시간대별 최소값을 담을 딕셔너리
SindorimQuitList = []    # 시간대별 최소값을 담을 딕셔너리
SindorimRideDic = {}    # 시간대별 최소값을 담을 딕셔너리
SindorimQuitDic = {}    # 시간대별 최소값을 담을 딕셔너리

# 승차와 하차 구별하기
SindorimRide = SindorimJanuary[SindorimJanuary['구분'] == '승차']
SindorimQuit = SindorimJanuary[SindorimJanuary['구분'] == '하차']

# 시간별 이용자 평균값 넣어주기
for time in times:
    SindorimRideDic[SindorimRide[time].mean()] = time
    SindorimQuitDic[SindorimQuit[time].mean()] = time
    SindorimRideList.append(SindorimRide[time].mean())
    SindorimQuitList.append(SindorimQuit[time].mean())

# 최소이용률 구하기
SindorimRideList.sort()
SindorimQuitList.sort()

# 이용객이 가장 적은 시간대 print
print("신도림역에서 승차가 제일 적은 시간은 : ", SindorimRideDic[SindorimRideList[0]])
print("신도림역에서 하차가 제일 적은 시간은 : ", SindorimQuitDic[SindorimQuitList[0]])
######################################################### 최소시간 구하기 END ##########################################

################################################### 요일 이용객 구하기 ###################################################
# 저장한 데이터 읽어오기
GangnamData = pd.read_excel('data/GangnamData.xlsx')
SindorimData = pd.read_excel('data/SindorimData.xlsx')

# 강남
GangnamRideMeanList = []    # 시간대별 최소값을 담을 딕셔너리
GangnamQuitMeanList = []    # 시간대별 최소값을 담을 딕셔너리


# 신도림
SindorimRideMeanList = []    # 시간대별 최소값을 담을 딕셔너리
SindorimQuitMeanList = []    # 시간대별 최소값을 담을 딕셔너리


# 7 ~ 9시 줄이기
for i in range(0, 2):
    GangnamData = GangnamData.drop(times[i], axis=1)
    SindorimData = SindorimData.drop(times[i], axis=1)
for i in range(4, len(times)):
    GangnamData = GangnamData.drop(times[i], axis=1)
    SindorimData = SindorimData.drop(times[i], axis=1)

# 월별로 나누기
for i in range(0, len(month)):
    # 강남 승차
    max = GangnamData[ GangnamData['날짜'] < pd.to_datetime(month[i])]    # 달별로 추리기
    max = max[max['구분'] == '승차']    # 승하차 구분
    max = max['합 계'].max()  # 승차에서 가장 많은거 추출
    maxWeek = GangnamData[ GangnamData['날짜'] < pd.to_datetime(month[i])]    # 달별로 다시 추리기
    maxWeek = maxWeek[maxWeek['합 계'] == max]    # 위에서 구한 max에 해방하는 구간 구하기
    maxWeek = pd.to_datetime(str(maxWeek['날짜'].min())).weekday()    # 해당구간의 datetime이용하여 요일구하기
    GangnamRideMeanList.append(maxWeek)

    # 강남 하차
    max = GangnamData[ GangnamData['날짜'] < pd.to_datetime(month[i])]
    max = max[max['구분'] == '하차']
    max = max['합 계'].max()
    maxWeek = GangnamData[GangnamData['날짜'] < pd.to_datetime(month[i])]
    maxWeek = maxWeek[maxWeek['합 계'] == max]
    maxWeek = pd.to_datetime(str(maxWeek['날짜'].min())).weekday()
    GangnamQuitMeanList.append(maxWeek)

    # 신도림 승차
    max = SindorimData[ SindorimData['날짜'] < pd.to_datetime(month[i])]
    max = max[max['구분'] == '승차']
    max = max['합 계'].max()
    maxWeek = SindorimData[SindorimData['날짜'] < pd.to_datetime(month[i])]
    maxWeek = maxWeek[maxWeek['합 계'] == max]
    maxWeek = pd.to_datetime(str(maxWeek['날짜'].min())).weekday()
    SindorimRideMeanList.append(maxWeek)

    # 신도림 하차
    max = SindorimData[ SindorimData['날짜'] < pd.to_datetime(month[i])]
    max = max[max['구분'] == '하차']
    max = max['합 계'].max()
    maxWeek = SindorimData[SindorimData['날짜'] < pd.to_datetime(month[i])]
    maxWeek = maxWeek[maxWeek['합 계'] == max]
    maxWeek = pd.to_datetime(str(maxWeek['날짜'].min())).weekday()
    SindorimQuitMeanList.append(maxWeek)

for i in range(0, len(month)):
    print("강남", i+1,'월 7 ~ 9시 가장 많은 승차 요일 : ', week[int(GangnamRideMeanList[i])])
    print("강남", i+1, '월 7 ~ 9시  가장 많은 하차 요일 : ', week[int(GangnamQuitMeanList[i])])
    print("신도림", i+1, '월 7 ~ 9시  가장 많은 승차 요일 : ', week[int(SindorimRideMeanList[i])])
    print("신도림", i+1, '월 7 ~ 9시  가장 많은 하차 요일 : ', week[int(SindorimQuitMeanList[i])])



################################################ 요일 이용객 구하기 END ##################################################


################################################### 1 ~ 12 최대인 날 ###################################################
# 저장한 데이터 읽어오기
GangnamData = pd.read_excel('data/GangnamData.xlsx')
SindorimData = pd.read_excel('data/SindorimData.xlsx')

# 7 ~ 9시 줄이기
for i in range(0,2):
    GangnamData = GangnamData.drop(times[i], axis=1)
    SindorimData = SindorimData.drop(times[i], axis=1)
for i in range(4,len(times)):
    GangnamData = GangnamData.drop(times[i], axis=1)
    SindorimData = SindorimData.drop(times[i], axis=1)

GangnamSum = {}    # 달마다 이용객을 담을 딕셔너리
SindorimSum = {}    # 달마다 이용객을 담을 딕셔너리
GangnamSumList = []    # 달마다 이용객을 담을 리스트
SindorimSumList = []    # 달마다 이용객을 담을 리스트

# 월별로 나누기
for i in range(0, len(month)):
    sum = GangnamData[ GangnamData['날짜'] < pd.to_datetime(month[i])]
    sum = sum['합 계'].sum()
    GangnamSum[sum] = i + 1
    GangnamSumList.append(sum)
    sum = SindorimData[SindorimData['날짜'] < pd.to_datetime(month[i])]
    sum = sum['합 계'].sum()
    SindorimSum[sum] = i + 1
    SindorimSumList.append(sum)

GangnamSumList.reverse()
SindorimSumList.reverse()


print("강남역에서 이용자가 제일 많은 달은 : ", GangnamSum[GangnamSumList[0]], '월')
print("신도림역에서 이용자가 제일 많은 달은 : ", SindorimSum[SindorimSumList[0]], '월')
################################################ 1 ~ 12 최대인 날 END ###################################################

