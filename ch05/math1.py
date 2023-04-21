# 수학 모듈 - math
# 원주율, 올림, 내림, 제곱근
import math

print(math.pi)             # 원주율
print(math.ceil(2.54))     # 정수로 올림
print(math.floor(4.923))   # 정수로 내림(버림)
print(int(math.sqrt(25)))  # 제곱근

# 내장 함수
print(round(11.78))
print(abs(-10))

# 절대값을 함수로 만들기
# 1. 0보다 작을 때 - 붙이기
"""
def my_abs(x):
    if x < 0:
        return -x
    else:
        return x


print(my_abs(-5))
print(my_abs(5))
"""
# 2. 제곱하여 양수를 만든 후 제곱근을 구함


def my_abs(x):
    y = x * x
    return math.sqrt(y)


print(int(my_abs(-5)))
print(int(my_abs(5)))
