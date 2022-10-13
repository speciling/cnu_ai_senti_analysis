import pprint
import requests
from bs4 import BeautifulSoup

url = 'https://news.daum.net/breakingnews/digital'
result = requests.get(url)

doc = BeautifulSoup(result.text, 'html.parser')

# <a herf="url"> : a태그는 클릭했을 때 해당 url로 이동
# len(): list의 갯수를 알려주는 함수
title_list = doc.select('ul.list_news2 a.link_txt')
# pprint.pprint(title_list)
# print(len(title_list))

# enumerate() : 반복하면서 index번호와 item을 가져옴
# list[]의 index는 0번부터 시작
# len(list) = 15, index = 0~14
for i, title in enumerate(title_list):
    print(f'인덱스: {i:-2d}, url: {title["href"]}')
