import requests
from bs4 import BeautifulSoup

url = 'https://n.news.naver.com/article/055/0001006655?cds=news_media_pc&type=editn'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, liek Gexko) Chrome/92.0.4515.131 Safari/537.36'}
result = requests.get(url, headers=headers)

doc = BeautifulSoup(result.text, 'html.parser')
title_list = doc.select('ul.type06_headline li')
print(title_list)