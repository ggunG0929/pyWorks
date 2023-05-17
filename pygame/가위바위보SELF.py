import random

print("♠ 가위 바위 보 게임 ♠")
random = random.randint(0, 2)
rsp = ["가위", "바위", "보"]
com = rsp[random]


def play():
    younum = 3  # 임의로 전역변수
    while younum == 3:
        you = input("당신: ")  # 문자인풋을 숫자처리
        if you == "가위":
            younum = 0
        elif you == "바위":
            younum = 1
        elif you == "보":
            younum = 2
        else:
            print("잘못된 입력입니다. 다시 입력해 주세요")
    print("컴퓨터: " + com)
    if younum == 0 and random == 2:
        state = 2
    elif younum == 2 and random == 0:
        state = 1
    else:
        state = random - younum
    print("결과: ", result[state])  # 딕셔너리의 키값으로 인덱싱


result = {0: '무승부', 1: '패', 2: '승'}  # 파이썬 딕셔너리로 인덱싱
state = 0  # 상태변수(0/1/2)

play()
