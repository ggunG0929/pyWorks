# turtle run 게임
import turtle as t
import random

# 적 거북이 생성
te = t.Turtle()
te.shape('turtle')
te.color('red')
te.speed(0)     #
te.up()
te.goto(0, 200)

# 주인공 거북이 생성
t.shape('turtle')
t.setup(500, 500)   # width, height
t.bgcolor('orange')
t.color('black')
t.speed(10)
t.up()

# 먹이 생성
tf = t.Turtle()
tf.shape('circle')
tf.color('yellow')
tf.speed(0)
tf.up()
tf.goto(0, -200)

# 초기 전역변수 세팅
score = 0
playing = False


def message(m1, m2):        # 메시지를 화면에 표시하는 함수
    t.clear()
    t.goto(0, 100)          # 첫번째 메시지 위치
    t.write(m1, False, "center", ("", 20))  # 아마도 객체, 글자가 끝나는 위치로 거북이가 이동할지 여부, 폰트[폰트명,사이즈]
    t.goto(0, -100)         # 두번째 메시지 위치
    t.write(m2, False, "center", ("", 12))
    t.home()    # 주인공 거북이가 첫위치로


def play():
    global score
    global playing
    t.forward(10)

    # 주인공 거북이가 먹이에 닿으면
    if t.distance(tf) < 12:
        score += 1  # 점수 상승
        t.write("+1")
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        tf.goto(x, y)  # 새로운 먹이 등장

    # 적 거북이와 닿으면
    if t.distance(te) < 12:
        text = "Score: " + str(score)
        message("Game Over", text)      # 위에 뜰 메시지와 아래에 뜰 메시지
        playing = False     # 초기화
        score = 0

    # 적 거북이가 방향을 쫓아오게
    if random.randint(1, 5) == 4:   # 방향을 알아챌 확률 20%
        ang = te.towards(t.pos())
        te.setheading(ang)

    # 적 거북이의 스피드 조정
    speed = score + 5   # 점수를 얻을 때마다 적거북이의 스피드가 빨라짐
    if speed > 10:
        speed = 10
    te.forward(speed)

    # 게임진행중
    if playing:
        t.ontimer(play, 100)    # 0.1초 간격으로 계속 play


def start():                # 게임을 시작하는 함수
    global playing          # playing 상태 가져옴
    if not playing:         # False일때
        playing = True      # playing 상태 변경(토글)
        t.clear()           # 시작메시지 지움
        play()              # 게임시작


# 방향조작
def turn_right():
    t.setheading(0)


def turn_up():
    t.setheading(90)


def turn_left():
    t.setheading(180)


def turn_down():
    t.setheading(270)


message("Turtle Run", "[Space]")    # 초기메시지
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, "space")
t.listen()

t.mainloop()
