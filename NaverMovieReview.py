# 네이버 영화를 수집 해주는 수집기

import requests
from bs4 import BeautifulSoup

################
# 영화 제목 수집 #
# ##############

# 함수 생성 후 호출


def movie_title_crawler(movie_code):
    url = f"https://movie.naver.com/movie/bi/mi/point.naver?code={movie_code}"
    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')
    title = doc.select('h3.h_movie > a')
    title = title[0].text
    return title


# 리뷰, 평점, 작성자 수집

def movie_review_crawler(movie_code):
    title = movie_title_crawler(movie_code)
    print(title)

    # set {제목, 리뷰, 평점}
