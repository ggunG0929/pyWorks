# turtle 모듈
import turtle as t

t.shape("turtle")

# 사각형을 그리며 이동
"""
t.forward(100)  # 직진 100px
t.left(90)      # 머리방향이 왼쪽으로 90도
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
"""
"""
for i in range(4):
    t.forward(100)
    t.left(90)
"""
# 삼각형을 그리며 이동
"""
t.color('blue')
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
"""
for i in range(4):
    t.forward(100)
    t.right(90)

t.color('blue')
for i in range(3):
    t.forward(100)
    t.left(120)

t.color('red')
t.pensize(3)
t.circle(50)    # 반지름이 50px인 원
"""
for i in range(5):
    t.forward(100)
    t.left(72)
"""
"""
for i in range(6):
    t.forward(100)
    t.left(60)
"""
t.mainloop()
