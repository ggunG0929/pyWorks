# GoldCustomer 클래스 생성
# 멤버 변수 - 고객 아이디, 이름, 등급, 보너스 포인트, 보너스 적립율
from classfication.customer.customer import Customer


class GoldCustomer(Customer):
    def __init__(self, cid, cname):
        super().__init__(cid, cname)
        self.cgrade = "Gold"
        self.sale_ratio = 0.1       # 10%
        # self.bonus_point = 0      # 따로 적지 않아도 상속됨
        self.bonus_ratio = 0.02     # 2%

    def calc_price(self, price):
        # 할인된 가격 = 원래가격 - (원래가격*구매할인율)
        price -= int(price * self.sale_ratio)       # 클래스 재정의 연습
        self.bonus_point += int(price * self.bonus_ratio)
        return price


g1 = GoldCustomer(1003, "뷔")
price = 10000
cost = g1.calc_price(price)

if __name__ == "__main__":
    print(f'{g1.getname()}님의 구매비용은 {cost}원입니다.')
    print(g1)
