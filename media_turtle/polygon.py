# 다각형 그리기
import turtle as t

t.shape('turtle')


# 매개변수 - 도형의 변의 개수
def polygon(n):
    for i in range(n):
        t.forward(50)
        t.left(360/n)


def polygon2(n, d):
    for i in range(n):
        t.forward(d)
        t.left(360/n)


polygon(3)
polygon(5)

t.up()      # 펜 올리기
t.forward(100)
t.down()    # 펜 내리기

polygon2(3, 100)
polygon2(5, 100)
"""
for i in range(3):
    t.forward(100)
    t.left(120)

t.up()      # 펜 올리기
t.left(90)
t.forward(100)
t.down()    # 펜 내리기

for i in range(3):
    t.forward(100)
    t.left(120)
    
t.up()
t.left(90)
t.forward(100)
t.down()
for i in range(4):
    t.forward(50)
    t.left(90)
"""
"""
# 임의로 그랑조
for i in range(3):
    t.forward(100)
    t.left(120)
t.up()
t.forward(50)
t.right(90)
t.forward(25)
t.left(150)
t.down()
for i in range(3):
    t.forward(100)
    t.left(120)
t.right(60)
t.circle(57)
"""
"""
for i in range(5):
    t.forward(100)
    t.right(145)
"""
# t.mainloop()
