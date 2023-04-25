# 영어 타자 게임
# 단어장 읽어오기
import random
import time

try:
    with open("./output/word.txt", 'r') as f:
        data = f.read().split()
    n = 1   # 문제 번호
    input("[타자 게임] 준비되면 엔터")
    start = time.time()
    count = 0   # 임의로 오타수 측정 추가
    while n <= 10:
        question = random.choice(data)
        print(f'문제 {n}')
        print(question)
        user = input()
        if question == user:
            n += 1
            print("통과!")
        else:
            count += 1
            print("오타! 다시 도전!")
    end = time.time()
    print(f'오타수: {count}회, 게임 소요 시간: {end-start:.2f}초')
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
