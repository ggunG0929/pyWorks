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


# 임의로 해 봄
a = 2
#int(input("상품의 종류가 몇 가지인지 입력하세요: "))
b = 5000
    #int(input("상품의 가격을 입력하세요: "))
c = 2
# int(input("상품의 개수를 입력하세요: "))
d = []
e = []
for i in range(1, a+1):
    d.append(b)
    e.append(c)
print(d)
print(e)

'''
a = input('몇 종류의 상품을 원하시나요?(상품의 종류 개수): ')

def get():
    b = []
    c = []
    for i in range(0, int(a)):
        b.append(int(input(f'{i+1}번째 상품의 가격을 입력해주세요: ')))
        c.append(int(input(f'{i+1}번째 상품의 주문 개수를 입력해주세요: ')))
    return b, c
get()

def calc():
    d = []
    s1 = 0
    s2 = 0
    for i in range(0, int(a)):
        s1 = b[i] * c[i]
        d.append(s1)
    for j in d:
            s2 += j
    return s2
calc()

def pull():
    global s2
    s3 = 0
    fee = 2500
    if s2 > 100000:
        s3 = s2 * 0.1
        return s2, s3
    elif s2 < 30000:
        s2 += fee
        return s2, fee
    else:
        return s2, s3
pull()

print()
print(f'고객님의 배송비는 {fee}원입니다.')
print(f'할인 금액은 {s3:.0f}원입니다.')
print(f'고객님의 총 결제 금액은 {s2}원입니다.')
'''
"""
# 쇼핑 주문, 할인, 배송비
a = {
    '선풍기': 90000, '튜브': 30000, '서핑보드': 65000, '나이키': 120000,
    '수박': 20000, '양말': 1200, '수영복': 40000, '팔토시': 13000,
    '에어컨': 1600000, '돼지고기': 10500, '소고기': 97000, '물안경': 2300
}
print('아래는 상품 목록입니다.')
for key, val in a.items():
    print(f'{key}: {val}')

b = input('몇 종류의 상품을 원하시나요?(상품의 종류 개수): ')
for i in range(0, int(b)):
    c = input('{}번째로 원하시는 상품을 입력해주세요: '.format(i+1))
    d = input(f"'{c}' 상품을 몇 개를 원하시나요?: ")
    s1 = int(a[c]) * int(d)
    e = []
    s1 = 0
    s2 = 0
    e.append(s1)
    s2 += e[i]

print(s2)
"""
