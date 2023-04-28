# pickle 모듈 사용
# 객체(리스트, 딕셔너리) 형태를 그대로 유지하여 저장하고 읽어옴
# pickle.dump - 쓰기, pickle.load - 읽기

import pickle

with open("./output/object.txt", "wb") as f:
    a = ['강아지', '고양이', '말']
    dic = {1: '강아지', 2: '고양이', 3: '말'}
    pickle.dump(a, f)   # 쓰기
    pickle.dump(dic, f)

with open("./output/object.txt", "rb") as f:    # 형태가 다른 것들이 같이 들어있으니(-종류가 같아도 합쳐지지 않음) 두번 뽑아야 종류 2가지가 다 보이는 듯
    c = pickle.load(f)  # 읽기
    d = pickle.load(f)
    print(c)
    print(d)
