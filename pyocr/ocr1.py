# 이미지 처리 - Pillow
from PIL import Image
from pytesseract import pytesseract

# 엔진
pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
img = Image.open("source/news.PNG")
img2 = Image.open("source/news2.PNG")
# img.show()

# text = pytesseract.image_to_string(img, lang="kor")
text2 = pytesseract.image_to_string(img2, lang="kor+eng")     # 영어도 읽으려면
# print(text)
# print(text.replace(" ", ""))    # 공백 제거
print(text2.replace(" ", ""))    # 공백 제거

# 변환된 텍스트를 파일에 쓰기
# encoding='utf-8' 꼭 명시해야 함
# with open("./output/news.text", 'w', encoding='utf-8') as f:
with open("./output/news2.text", 'w', encoding='utf-8') as f:
    # f.write(text)
    # f.write(text.replace(" ", ""))
    f.write(text2.replace(" ", ""))
