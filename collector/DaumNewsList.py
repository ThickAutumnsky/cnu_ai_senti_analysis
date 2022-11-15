import requests
from bs4 import BeautifulSoup
import CollectorService
import pprint

url = "https://news.daum.net/breakingnews/digital?page="

result = requests.get(url)

doc = BeautifulSoup(result.text,"html.parser")

title_list = doc.select('ul.list_news2 a.link_txt')
# pprint.pprint(title_list)
# pprint.pprint(len(title_list))
# len() 리스트 길이 함수
# list의 인덱스는 0부터 시작

pagenum = 0
while pagenum<23:
    pagenum = pagenum+1
    url1 = url + str(pagenum)
    result = requests.get(url1)

    doc = BeautifulSoup(result.text, "html.parser")

    title_list = doc.select('ul.list_news2 a.link_txt')

    for i, title in enumerate(title_list):
        print(f'page:{pagenum}index:{i},링크:{title["href"]}')
        print(CollectorService.get_daum_news(title["href"]))
