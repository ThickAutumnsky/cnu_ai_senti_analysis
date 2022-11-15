# https://news.daum.net/breakingnews/digital?page=1
# 쿼리스트링(QueryString): url+data
# ? 전까지 url, ? 뒤로 데이터
import requests
from bs4 import BeautifulSoup
import CollectorService

url = "https://news.daum.net/breakingnews/digital?page="

# range(시작값,끝값, 크기)
# 크기 생략 가능
# range(1,3,1) = [1,2]
# range(1,10,2) = [1,3,5,7,9]

newsnum = 0;
for num in range(1,3):

    # pprint.pprint(title_list)
    # pprint.pprint(len(title_list))
    # len() 리스트 길이 함수
    # list의 인덱스는 0부터 시작

    url1 = url + str(num)
    result = requests.get(url1)

    doc = BeautifulSoup(result.text, "html.parser")

    title_list = doc.select('ul.list_news2 a.link_txt')
    if len(title_list) == 0:
        exit()

    for i, title in enumerate(title_list):
        print(f'page:{num} index:{i},링크:{title["href"]}')
        newsnum += 1
        print(CollectorService.get_daum_news(title["href"]))
    print("=================================================================================================")

print(f'총{newsnum}개의 뉴스 수집.')
exit()
