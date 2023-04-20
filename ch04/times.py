# 배수를 구하는 함수를 정의하고 사용
# 배수의 개수 구하기
"""
# 내답
def duple(num):
    for i in range(1, 101):
        j = num*i
        if j > 100:
            print(f'배수의 개수: {i-1}')
            break
        else:
            print(j, end=' ')


duple(3)
"""
# 선생님답
"""
def times(x):
    count = 0   # 지역 변수
    for i in range(1,101):
        if i % x == 0:
            count += 1
            print(i, end=' ')
    print(f'\n배수의 개수: {count}')
"""


def times(x):
    global count    # 전역 변수
    for i in range(1, 101):
        if i % x == 0:
            count += 1
            print(i, end=' ')
    print(f'\n배수의 개수: {count}')


count = 0
times(3)
