# season 파일 읽기 # 임의로 만듬 with as
try:
    with open("c:/pyfile/season.txt", 'r') as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
