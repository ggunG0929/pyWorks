# 거북이 대포 게임
"""
1. 키보드 방향키로 발사 각도 조절
2. 스페이스바로 발사
3. 화살촉 모양의 포탄이 하늘로 날아감
"""
import turtle as t
import random


def turn_up():      # 위쪽 화살표 키
    t.left(2)


def turn_down():    # 아래쪽 화살표 키
    t.right(2)


def fire():
    ang = t.heading()     # 거북이가 현재 바라보는 각도
    while t.ycor() > 2:     # y좌표가 0보다 크면 - 포탄이 땅 위에 있는 동안
        t.forward(15)
        t.right(5)

    d = t.distance(target, 0)
    t.sety(random.randint(10, 100))     # y좌표 - 성공 또는 실패를 표시할 위치
    if d < 25:  # 명중 - 목표지점에 닿음
        t.color('blue')
        t.hideturtle()
        t.write('Good!', False, "center", ("", 15))
    else:       # 목표 지점에 닿지 않았을 때
        t.color('red')
        t.write('Try again!', False, "right", ("", 15))  # 두번째 항목 : 글자가 끝나는 위치로 거북이가 이동할지 여부 / 세번째 항목 : t의 위치가 글자의 오른쪽이나 왼쪽이나 중간
        t.color('black')
        t.goto(-200, 10)
        t.setheading(ang)   # 기억된 머리 각도 설정


# 땅 그리기
t.hideturtle()
t.up()
t.goto(-300, 0)
t.down()
t.goto(300, 0)

# 목표 지점 설정
target = random.randint(50, 150)    # 50~150사이의 x좌표 한 지점
t.color('green')
t.pensize(2)
t.up()
t.showturtle()
# 목표 지점의 길이 - 50px
t.goto(target-25, 2)    # target = 100, 100-25 = 75
t.down()
t.goto(target+25, 2)    # target = 100, 100+25 = 125

# 포탄의 처음 위치
t.color('black')
t.up()
t.goto(-200, 10)
t.setheading(20)

# 거북이 대포가 동작하는 데 필요한 설정
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")    # space키 누르면 발사
t.listen()

t.mainloop()
