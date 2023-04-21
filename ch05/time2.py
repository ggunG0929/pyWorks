# time 모듈2
import time

# 1부터 10까지 출력 - 1초 간격으로 출력
start = time.time()
for i in range(1, 11):
    time.sleep(1)
    print(i)
end = time.time()
print("수행 시간: {:.2f}".format(end - start))
