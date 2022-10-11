#print("Hello")


# import 와 Library(module)
#   1. Built in Library Python 설치하면 자동으로 제공
#       math, svs, os 등
#   2. 외부 Library: 직접 추가해서 사용.
#       request, beautifulsoup4 등
#
# 외부 라이브러리 사용하기 위해서는 import 작업 진행
#   도서관에서 필요한 책을 빌려오는 개념
#

import requests # 책 전체를 빌려옴
from bs4 import BeautifulSoup # bs4라는 책에서 BeautifulSoup만 빌려옴

# 다음 뉴스 웹페이지에서 제목과 내용(본문) 데이터 수집
# 1.url:https://v.daum.net/v/20221006105157803

url = 'https://v.daum.net/v/20221006105157803'

# 2. request로 해당 url의 html 전체 코드를 수집

result = requests.get(url)

#print(result.text)

doc = BeautifulSoup(result.text,"html.parser")
title = doc.select("h3.tit_view")
title = title[0].text

print(f'뉴스제목:{title}')

article = doc.select("div.news_view fs_type1")

#python은 []:List Type
# index 0 1 2 3 4
# [5,6,9,10,15]
# [5]