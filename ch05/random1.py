# random 모듈
# 숫자(정수)를 랜덤 추출 - random.randint(1, 10)
# 리스트에서 요소 추출 - random.choice(리스트)
import random

# 1 ~ 10 중 무작위로 추출
num = random.randint(1, 10)
print(num)

# 주사위 만들기
dice = random.randint(1, 6)
print(dice)

# 주사위 10번 던지기
for i in range(10):     # 0~9까지 총 10번
    dice = random.randint(1, 6)
    print(dice)

# 리스트에서 랜덤하게 값을 추출하기
과일 = ['딸기', '수박', '참외', '사과']
#print(과일[0])
#print(과일[-1])
print(random.choice(과일))

# 주사위 2개를 10번 던지기
# 두 눈의 합이 7이면 "Seven Thrown!!" 출력, 11이면 "Eleven Thrown!!"
# 두 눈의 수가 같으면 "Double Thrown!!" 출력
for i in range(10):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"{dice1},{dice2}", end=' ')
    if dice1 + dice2 == 7:
        print("⇒ Seven Thrown!!")
    elif dice1 + dice2 == 11:   # 선생님은 if를 쓰심
        print("⇒ Eleven Thrown!!")
    elif dice1 == dice2:
        print("⇒ Double Thrown!!")
