import requests
from bs4 import BeautifulSoup

url = "https://n.news.naver.com/mnews/article/366/0000846967?sid=105"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

h = {'yuio'}

result = requests.get(url,headers=headers)
# print(result)
doc = BeautifulSoup(result.text,'html.parser')
title_List = doc.select('ul.type06_headline li')
