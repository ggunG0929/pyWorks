# for ~ in range()
# 1부터 10까지 출력
# range(시작값, 종료값, 증감값)
'''
for i in range(1,11,1):
    print(i, end='') # i값을 한 줄씩 입력하지 않고 옆으로 나열해서 출력
print()
for i in range(10,0,-1):
    print(i, end='')
print()
'''
# 1부터 10까지의 합계
''''
sum_v=0
for i in range(1,11): # 1은 생략가능
    sum_v+=i
    print(f"i={i}, sum_v={sum_v}")
print(f"합계: {sum_v}")
'''
# 1부터 10까지의 홀수 출력
'''
# 내답
for i in range(1,11,2):
    print(i)
# 선생님답
for i in range(1,11,1):
    if i%2==1:
        print(i, end=" ")
'''

num=[10,50,30,70]
print(50 in num)
print(80 in num)
# 리스트 출력
print(num)
# 전체 요소를 출력
for i in num:
    print(i)

# 50보다 큰 수를 출력
for i in num:
    if i>50:
        print(f"50보다 큰 수는 {i}")

city = ["Seoul","Incheon","Gwangju"]
for i in city:
    # print(i)
    print(i[0],end='') # 내용 중 0번째 글자
'''
# city[0]: 첫번째 i seoul -> i[0] - 'S'
# city[1]: 두번째 i incheon -> i[0] - 'I'
# city[2]: 세번째 i gwangju -> i[0] - 'G'
'''
