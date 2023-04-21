# 키보드로 거북이 조종하기

import turtle as t


def turn_right():
    t.setheading(0)
    t.forward(10)


def turn_up():
    t.setheading(90)
    t.forward(10)


def turn_left():
    t.setheading(180)
    t.forward(10)


def turn_down():
    t.setheading(270)
    t.forward(10)


def clear():
    t.clear()   # 화면 지우기


def space():
    t.forward(100)  #임의로 추가


t.shape('turtle')
t.color('green')
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(clear, "Escape")
t.onkeypress(space, "space")    # 임의로 추가

t.listen()  # 키 작동을 대기중

t.mainloop()
