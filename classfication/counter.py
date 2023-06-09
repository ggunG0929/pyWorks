# 객체 지향 언어 - 캡슐화(정보은닉), 상속, 다형성
# Counter 클래스 만들기
# 멤버 변수에 직접 접근하지 않음 - 정보 은닉(캡슐화)
# 함수 안에 멤버 변수를 작성 - set(), get()
# 외부에서는 함수에 접근
class Counter:
    x = 0   # 클래스 변수 (def 밖에)

    def __init__(self):
        Counter.x += 1  # 클래스변수이므로 클래스로 직접 접근

    def get_count(self):
        return Counter.x


c1 = Counter()
# print(c1.x)   # 멤버변수에 접근하지 않음
print(c1.get_count())   # 1

c2 = Counter()
# print(c2.x)   # 2
print(c2.get_count())   # 2

c3 = Counter()
# print(c3.x)   # 3
print(c3.get_count())   # 3
"""
class Counter:
    def __init__(self):
        self.x = 0      # 인스턴스 변수
        self.x += 1     # x에 1증가

    def get_count(self):
        return self.x


c1 = Counter()  # 객체 생성
print(c1.get_count())   # 1

c2 = Counter()
print(c2.get_count())   # 1
"""
