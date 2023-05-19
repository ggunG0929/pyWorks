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
    state = random - younum     # 2랑 -2의 경우도 결국엔 승과 패로 인덱싱 되기 때문에 연산작업 필요x
    print("결과: ", result[state])  # 딕셔너리의 키값으로 인덱싱


result = {0: '무승부', 1: '패', 2: '승'}  # 파이썬 딕셔너리로 인덱싱
state = 0  # 상태변수(0/1/2)

play()

"""
디버깅
가위바위보 - 0 1 2

com     you: 가위 0
가위 0 무승부 com-you = 0
바위 1 패    com-you = 1
보  2 승     com-you = 2

com     you: 바위 1
가위 0 승     com-you = -1
바위 1 무승부 com-you = 0
보  2 패     com-you = 1

com     you: 보 2
가위 0 패    com-you = -2
바위 1 승    com-you = -1
보  2 무승부 com-you = 0

com-you
무승부 0
패    1, -2(마지막에서 두번째 번호인 1로 감)
승    2, -1(맨마지막 번호인 2로 감)

{0: '무승부', 1: '패', 2: '승'}
"""
