# naver에서 필요한 정보 가져오기
import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com/"
response = requests.get(url)
# print(response.text)    # 들여쓰기 포함
html = BeautifulSoup(response.text, 'html.parser')
# print(html)     # 들여쓰기 미포함
print(html.title)   # <title> 태그 - <title>NAVER</title>
print(html.title.name)  # 태그 이름 - title
print(html.title.text)  # 태그 문자열 - NAVER

# '네이버를 시작페이지로' 문자열 찾아오기
div = html.find('div', attrs={'class': 'service_area'})
first_a = div.find('a')
print(first_a)
print(first_a.text)

# '쥬니어네이버' 찾아오기
# 내답
# j_n = html.find('a', attrs={'class': 'link_jrnaver'})
# jn = j_n.find('span')
# print(jn)
# print(jn.text)
# 선생님답
all_a = div.findAll('a')
print(all_a[1])
print(all_a[1].text)    # 쥬니어네이버

for a in all_a:     # 네이버를 시작페이지로/ 쥬니어네이버/ 해피빈
    print(a)        # 각각의 <a> 태그
    print(a.text)   # 각각의 텍스트
