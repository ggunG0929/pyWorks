# 영어 단어장 만들기
import random
try:
    word = ['ant', 'bear', 'chicken', 'deer', 'elephant', 'fox', 'horse', 'lion', 'monkey', 'penguin']
    with open("./output/word.txt", 'w') as f:
        for i in word:
            if i == word[-1]:
                f.write(i)
            else:   # else로 분리해서 마지막에 공백을 제거하지 않으면, 아래에서 split(' ') 했을 때 공백부분이 리스트에 추가됨
                f.write(i + ' ')
except FileNotFoundError:
    print("파일을 쓸 수 없습니다.")

# 파일 읽기
try:
    with open("./output/word.txt", 'r') as f:
        data = f.read().split(' ')     # 공백문자(' ')로 구분 -> 리스트로 변환     # split()도 가능
        #word = random.choice(data)  # 단어 1개 랜덤 추출
        print(data)
except FileNotFoundError:
    print("파일을 읽을 수 없습니다.")
