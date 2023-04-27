# map(), filter()
# list()함수로 리스트를 반환함
def times(i):
    return 3 * i


v = [1, 2, 3, 4]
# times = lambda x: 3 * x
# map(함수, 리스트) : 리스트를 함수에 넣어서 출력
result = map(times, v)
print(list(result))


# filter()와 lambda사용
# 음의 정수를 출력하시오
def negative(n):
    return n < 0


li = [-5, 1, 2, -11, 76]
# negative = lambda x: x < 0
value = filter(negative, li)    # filter(함수, 리스트) : 리스트 중 함수에 해당하는 값만 출력
print(list(value))
