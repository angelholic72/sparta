import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
##headers: URL을 가져올때 사람인것 처럼 하려고 써준
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20191207',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.


soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#old_content > table > tbody > tr')

#old_content > table > tbody > tr:nth-child(2) > td.title > div
for tr in trs:
    title = tr.select_one('td.title > div > a')
    if title is not None:
        star = tr.select_one('td.point')
        rank = tr.select_one('td:nth-child(1) > img')

        doc = {
            'rank':rank['alt'],
            'title':title.text,
            'star':star.text
        }

        db.movies.insert_one(doc)




        ## title이 none이 아니면 이라는 문법

#############################
# (입맛에 맞게 코딩)
#############################