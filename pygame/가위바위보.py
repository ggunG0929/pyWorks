# ★ 가위, 바위, 보 게임 만들기
"""
-게임 방법
1. 당신(you)은 가위, 바위, 보 중 하나를 입력한다.
2. 컴퓨터(com)는 가위, 바위, 보 중 하나를 랜덤 생성한다.
3. 결과 출력은 무승부, 패, 승이다.
4. 잘못 입력한 경우 "잘못된 입력입니다. 다시 입력해 주세요"
"""
import random

print("♠ 가위 바위 보 게임 ♠")
younum = 3
while younum == 3:
    you = input("당신: ")
    if you == "가위":
        younum = 0
    elif you == "바위":
        younum = 1
    elif you == "보":
        younum = 2
    else:
        print("잘못된 입력입니다. 다시 입력해 주세요")
random = random.randint(0, 2)
rsp = ["가위", "바위", "보"]
com = rsp[random]
print("컴퓨터: " + com)
if younum == random:
    result = "무승부"
elif younum == random + 1 or (younum == 0 and random == 2):
    result = "승"
elif younum == random - 1 or (younum == 2 and random == 0):
    result = "패"
else:
    result = "오류가 발생했습니다."
print("결과: " + result)

"""
# 선생님답
you = input("당신: ")
rsp = ["가위", "바위", "보"]
com = random.choice(rsp)
print("컴퓨터: " + com)

if you not in rsp:
    print("잘못된 입력입니다. 다시 입력해 주세요")
    sys.exit(0)  # 프로그램 즉시 종료

if you == com:
    print('결과 : 무승부')
elif you == '가위' and com == '보':
    print('결과 : win')
elif you == '바위' and com == '가위':
    print('결과 : win')
elif you == '보' and com == '바위':
    print('결과 : win')
else:
    print('결과 : lose')
"""
