import requests
from bs4 import BeautifulSoup
import pprint

url = "https://news.daum.net/breakingnews/digital"

result = requests.get(url)

doc = BeautifulSoup(result.text,"html.parser")

title_list = doc.select('ul.list_news2 a.link_txt')
# pprint.pprint(title_list)
# pprint.pprint(len(title_list))
# len() 리스트 길이 함수
# list의 인덱스는 0부터 시작

for i, title in enumerate(title_list):
    print(f'index:{i}, 제목{title.get_text()}')
