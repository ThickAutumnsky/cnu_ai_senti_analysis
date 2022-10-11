import requests
from bs4 import BeautifulSoup

url = "https://n.news.naver.com/mnews/article/020/0003455573?sid=105"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
h = {'yuio'}

result = requests.get(url,headers=headers)

# print(result.text)

doc = BeautifulSoup(result.text,"html.parser")
title = doc.select("h2.media_end_head_headline")[0].get_text()
print(f'제목:{title}')

article = doc.select("div.newsct_body")

print(article[0].text)
