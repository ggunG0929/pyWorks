# textdb -> book테이블
import sqlite3


def getconn():
    conn = sqlite3.connect("c:/green_project/sqlworks/pydb/testdb.db")
    return conn


# 테이블 생성
def create():
    conn = getconn()
    cursor = conn.cursor()  # cursor 객체는 sql을 조작함   # autoincrement -> sequence
    sql = """
        CREATE TABLE book(
            book_no INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            page INTEGER
        )
    """
    cursor.execute(sql)     # 실행
    conn.commit()   # 커밋 완료
    conn.close()


# 책 추가
def insert():
    conn = getconn()
    cursor = conn.cursor()
    # 줄바꿀시 마지막에 띄어쓰기 포함하기
    sql = "INSERT INTO book(title, author, page) " \
          "VALUES(?, ?, ?)"
    # cursor.execute(sql, ('혼자 공부하는 자바', '신용권', 600))
    cursor.execute(sql, ('python projects', '켄 유엔스', 500))
    conn.commit()
    conn.close()


# 책 전체 검색
def select():
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM book"
    cursor.execute(sql)
    rs = cursor.fetchall()  # 여러개 가져오기
    # print(rs)   # 리스트로 출력
    for i in rs:
        print(i)    # 튜플로 출력
    conn.close()    # commit 안해도 됨


# 책 1권 검색
def select_one():
    conn = getconn()
    cursor = conn.cursor()
    # 동적 바인딩 방식(물음표 사용)
    sql = "SELECT * FROM book WHERE book_no = ?"
    cursor.execute(sql, (2, ))  # 튜플 자료구조이므로 1개일 때 쉼표 사용
    rs = cursor.fetchone()  # 하나 가져오기
    print(rs)
    conn.close()    # commit 안해도 됨


# 책 수정
def update():
    conn = getconn()
    cursor = conn.cursor()
    # 책번호가 2인 책의 page를 650 page로 변경하기
    sql = "UPDATE book SET page = ? WHERE book_no = ?"
    cursor.execute(sql, (650, 2))   # 두개 이상부터는 마지막에 굳이 쉼표 안 써도 되는 듯
    conn.commit()
    conn.close()


def delete():
    conn = getconn()
    cursor = conn.cursor()
    # 책번호가 1인 책 삭제
    sql = "DELETE FROM book WHERE book_no = ?"
    cursor.execute(sql, (1, ))
    conn.commit()
    conn.close()


# print(getconn(), "연결 객체 생성")
# create()
# insert()
# update()
delete()
select()
# select_one()
