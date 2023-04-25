# 함수 - function, method(메서드)
# 1부터 10까지 출력
"""
for i in range(1, 11):
    print(i)
"""
import time


# 1부터 n까지 출력 함수
def get_num(n):
    for i in range(1, n+1):
        print(i, end=' ')


if __name__ == "__main__":
    get_num(10)
    print()

start1 = time.time()


# 1부터 n까지 합계를 구하는 함수
def get_sum(n):
    sum_v = 0
    for i in range(1, n+1):
        sum_v += i
    return sum_v


if __name__ == "__main__":
    print(f'합계: {get_sum(1000000)}')
    end1 = time.time()
    print(f'함수 1의 소요시간: {end1 - start1}초')
    start2 = time.time()


# 계산 복잡도 - 곱셈, 덧셈, 나눗셈 - 3번: O(1)
def get_sum2(n):    # 숫자가 커지면 함수1에 비해서 속도가 빠름, 계산복잡도가 n과 무관함
    sum_v = n * (n+1) // 2
    return sum_v


if __name__ == "__main__":
    print(f'합계: {get_sum2(1000000)}')
    end2 = time.time()
    print(f'함수 2의 소요시간: {end2 - start2}초')
