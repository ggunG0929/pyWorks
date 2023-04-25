# Person 클래스
class Person:
    def __init__(self, name, age):
        self.name = name    # 생성자 (함수)
        self.age = age      # 자바의 경우 self가 아니라 this

    # 멤버의 정보
    def __str__(self):
        return f'이름: {self.name}, 나이: {self.age}'


# 상속 - 자식클래스이름(부모클래스이름)
class Employee(Person):     # Person 상속
    def __init__(self, name, age, id):      # 부모것, 자식것
        super().__init__(name, age)         # 부모것 설정
        self.id = id                        # 자식것 설정 - 사번 초기화

    # 메서드 재정의(오버라이딩)
    def __str__(self):
        #return f'이름: {self.name}, 나이: {self.age}, 사번: {self.id}'
        return f'{super().__str__()}, 사번: {self.id}'

    def work(self):
        print("회사에 다닙니다.")


e1 = Employee("이하나", 25, 'a1001')
print(e1)
e1.work()

"""
# 클래스 사용 - 객체 생성(메모리 실행)
# p1 - 인스턴스, 오브젝트
p1 = Person("김산", 21)
#print(p1.name)
#print(p1.age)
print(p1)

p2 = Person("이강", 30)
#print(p2.name)
#print(p2.age)
print(p2)
"""
