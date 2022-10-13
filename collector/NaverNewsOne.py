import requests
from bs4 import BeautifulSoup

url = 'https://n.news.naver.com/mnews/article/138/0002134270?sid=105'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, liek Gexko) Chrome/92.0.4515.131 Safari/537.36'}
result = requests.get(url, headers=headers)
doc = BeautifulSoup(result.text, 'html.parser')

# get_text() : 태그를 제거하고 text만 추출
# strip() : 앞 뒤 공백을 제거
title = doc.select('h2.media_end_head_headline')[0].get_text()
content = doc.select('div#dic_area')[0].get_text().strip()
print(f'본문: {title}')  # fstring
print('내용: {}'.format(content))  # format

