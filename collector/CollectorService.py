########################################
# collector 비지니스 로직을 모아둔 파이썬 파일
########################################
# - 2022.10.18 이민후
########################################

import requests
from bs4 import BeautifulSoup

# 함수 생성
# 함수: 반복적으로 사용하는 기능을 코드로 묶어서 만듬.
#   사용: 함수 이름으로 호출
# print() 등.
# 사용자 정의 함수: 직접 만든 함수
# 내장 함수: 기본 함수
# 외부 함수: 다른 개발자가 만든것


def get_daum_news(url):

    result = requests.get(url)

    doc = BeautifulSoup(result.text, "html.parser")
    title = doc.select("h3.tit_view")
    try:
        title = title[0].text
    except:
        title = '\n'
    # print(f'뉴스제목:{title}')

    contents = doc.select("section p")
    content = ""

    if len(contents) != 0:
        for line in contents:
           content += line.get_text()
    # print(f'내용:{content}')

    return (f'제목:{title},내용:{content}')

# python naming rule
# 파스칼-> GetDaumNews
# 카멜 -> getDaumNews
# 스네이크 -> get_daum_news
