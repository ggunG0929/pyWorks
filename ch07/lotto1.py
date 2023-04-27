# 로또 복권 추첨 프로그램
# 1~45까지 6개 랜덤수로 저장
import random

# 빈 리스트 생성
lotto = []
# 처리
while len(lotto) < 6:   # lotto의 개수가 6개일 때 빠져나옴
    num = random.randint(1, 45)
    if num not in lotto:    # 중복 제거
        lotto.append(num)
"""
for i in range(6):
    num = random.randint(1, 45)
    if num not in lotto:    # 중복 제거
        lotto.append(num)
"""
    # 임의로 정렬
for i in range(6):
    for j in range(i+1, 6):
        if lotto[i] > lotto[j]:
            temp = lotto[i]
            lotto[i] = lotto[j]
            lotto[j] = temp
# 출력
print(lotto)

# 임의로 검색 :
lotto2 = random.sample(range(1, 45), 6)     # random.sample - 중복없이 숫자를 뽑아줌
lotto2.sort()                               # 리스트.sort() - 작은수부터 정렬, 반대로 하고 싶으면 괄호안에 reverse=true 입력
print(lotto2)
