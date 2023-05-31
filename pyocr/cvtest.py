import cv2

img = cv2.imread("./source/cat.jpg", cv2.IMREAD_COLOR)      # 컬러로 가져오기
cv2.imshow('cat', img)      # imshow(제목, 이미지파일)
cv2.waitKey(2000)      # 0 - 계속 대기, 2000 - 2초 후 꺼짐

# 파일 쓰기(복사)
cv2.imwrite('./source/cat2.jpg', img)   # imwrite(경로, 파일)

# 회색 스타일 수정(RGB-> BGR)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)            # 흑백으로 컨버팅
cv2.imshow('cat', img_gray)
cv2.waitKey(2000)

# 파일 쓰기(복사)
cv2.imwrite('./source/cat3.jpg', img)
