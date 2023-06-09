# SuperSonicAirplane 클래스 생성
from classfication.airplain import Airplane


# Airplane을 상속 받음
class SuperSonicAirplane(Airplane):
    # 1번 - NORMAL, 2번 - SUPERSONIC
    NORMAL = 1      # 상수 설정(대문자)
    SUPERSONIC = 2

    # 모드 - 멤버 변수
    def __init__(self):
        self.fly_mode = SuperSonicAirplane.NORMAL

    def fly(self):
        if self.fly_mode == SuperSonicAirplane.SUPERSONIC:
            print("비행기가 초음속으로 비행합니다.")
        else:
            super().fly()


sa = SuperSonicAirplane()
sa.take_off()
sa.fly()
sa.fly_mode = SuperSonicAirplane.SUPERSONIC     # 모드 변경
sa.fly()
sa.land()
