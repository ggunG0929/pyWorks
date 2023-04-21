# 시간 - time 모듈
import time

# 1970. 1. 1 자정 이후 지금까지 시간을 초로 환산
print(time.time())

# round() - 정수로 반올림, 괄호 안에 콤머표시 후 자리수 지정 가능
year = round(time.time()/(365*24*60*60))
day = round(time.time()/(24*60*60))
print(year)
print(day)

# 시간 정보 - 연도, 월, 일, 시, 분, 초, 요일, 1월 1일부터 며칠
print(time.localtime())
# 날짜와 시간 형태로 표시 - 요일, 월, 일, 시간, 연도
print(time.ctime())

# 시간 측정
# 종료 시간(time.time()) - 시작 시간(time.time())
# time.sleep(1) - 1초 대기
# 1~1,000,000(백만) 출력시 걸리는 시간
start = time.time()
for i in range(1, 1000001):
    print(i)

end = time.time()
print(f'{end - start:.3f}')
