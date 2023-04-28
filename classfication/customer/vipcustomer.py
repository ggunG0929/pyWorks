# VIPCustomer 클래스 - Customer를 상속 받음
from classfication.customer.customer import Customer


class VIPCustomer(Customer):
    def __init__(self, cid, cname, agent):  # agent 추가
        super().__init__(cid, cname)
        self.agent = agent
        self.cgrade = "VIP"
        self.sale_ratio = 0.1       # 10%
        self.bonus_ratio = 0.05     # 5%

    def calc_price(self, price):
        # 할인된 가격 = 원래가격 - (원래가격*구매할인율)
        price -= int(price * self.sale_ratio)       # 클래스 재정의 연습
        self.bonus_point += int(price * self.bonus_ratio)
        return price

    def __str__(self):
        return f'{super().__str__()}\n전문 상담원 ID는 {self.agent}입니다.'


vip = VIPCustomer(1004, '진', 777)
price = 10000
cost = vip.calc_price(price)
if __name__ == "__main__":
    print(f'{vip.getname()}님의 구매비용은 {cost}원입니다.')
    print(vip)
