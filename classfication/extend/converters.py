# ScaleConverter 상속받는 클래스
# import 패키지(폴더?)이름.모듈(파일)이름
import classfication.scale_converter
# from 패키지(폴더)이름.모듈(파일)이름 import 클래스(함수)
from classfication.scale_converter import ScaleConverter
con = ScaleConverter("KB", "B", 1024)
if __name__ == "__main__":
    print("Converting 1KB")
    print("= " + str(con.convert(1)) + con.units_to)


# 화씨온도(F) = 섭씨온도(C) X 1.8 +32
class Converter(ScaleConverter):
    def __init__(self, units_from, units_to, factor, offset):
        super().__init__(units_from, units_to, factor)  # 부모멤버 상속받음
        self.offset = offset

    def convert(self, value):   # 함수 이름은 같으나 내용을 재정의
        #return self.factor * value + self.offset
        return super().convert(value) + self.offset


if __name__ == "__main__":
    conv = Converter('C', 'F', 1.8, 32)
    print("Converting 21C")
    print(f'= {conv.convert(21):.2f}{conv.units_to}')
