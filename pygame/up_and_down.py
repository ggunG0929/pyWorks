# 숫자 추측게임
"""
게임 방법
- 게임이 시작되면 컴퓨터가 난수(정답)를 생성한다.
- 사용자의 추측값이 정답과 같으면 '정답!',
    추측값이 정답보다 크면 "너무 커요!",
    추측값이 정답보다 작으면 "너무 작아요!" 출력
"""
import random

min_v = 1
max_v = 100
com = random.randint(min_v, max_v)
"""
while True:
    you = int(input(f"맞혀보세요({min_v}~{max_v}): "))
    if com == you:
        print(f"정답! {com}")
        break
    elif com > you:
        print("너무 작아요!")
        min_v = you     # 추측값을 최소값으로 설정
    elif com < you:
        print("너무 커요!")
        max_v = you     # 추측값을 최대값으로 설정
    else:
        print("입력을 확인하세요")
"""
"""
try:
    for i in range(0, 10):
        you = int(input(f"맞혀보세요([{i+1}회]{min_v}~{max_v}) > "))
        if you > 100 or you < 1:
            print("입력 범위가 아니에요. 다시 입력해 주세요.")
        elif com == you:
            print(f"정답! {com}")
            break
        elif com > you:
            print("너무 작아요!")
            min_v = you     # 추측값을 최소값으로 설정
        else:
            print("너무 커요!")
            max_v = you     # 추측값을 최대값으로 설정
    print(f"점수: {(10-i)*10}점")
except ValueError:
    print("유효한 숫자가 아닙니다. 다시 입력해주세요.")
"""
# 내 답
count = 0
while count != 10:
    try:
        you = int(input(f"맞혀보세요[{count+1}회]({min_v}~{max_v}): "))
        count += 1
        if com == you:
            print(f"정답! {com}")
            break
        elif com > you:
            print("너무 작아요!")
            min_v = you
        elif com < you:
            print("너무 커요!")
            max_v = you
        else:
            print("입력을 확인하세요")
    except ValueError:
        print("유효한 입력이 아닙니다. 다시 입력해주세요.")
if count == 10:
    print("횟수를 모두 소진하였습니다.")
    print(f"정답: {com}")
print(f"점수: {(11-count)*10}")
