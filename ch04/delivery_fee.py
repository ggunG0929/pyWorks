# 배송비 계산
# 주문 상품 가격이 2만원 미만이면 배송비 2500원 포함
# 2만원 이상이면 배송비를 포함하지 않는 프로그램
"""
price = 25000
delivery_fee = 2500

if price < 20000:
    price = price + delivery_fee
else:
    price


print(price)
"""


def get_price(unit_price, num):  # 매개변수 - 단위가격, 수량
    delivery_fee = 2500          # 배송비
    price = unit_price*num       # 주문가격 = 단위가격 x 수량
    if price < 20000:
        price += delivery_fee
        return price
    else:
        return price


order1 = get_price(15000, 2)
order2 = get_price(5000, 3)
print(f'주문 1의 가격은 {order1}원 입니다.')
print(f'주문 2의 가격은 {order2}원 입니다.')
