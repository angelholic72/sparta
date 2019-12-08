import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20191208',headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                   # 'dbsparta'라는 이름의 db를 만듭니다.

#순위/곡제목/가수
##body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
##body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
##body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis


songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')


for song in songs:
    rank = song.select_one('td.number').text.split(' ')[0]
    title = song.select_one('td.info > a.title.ellipsis').text.strip()
    artist = song.select_one('td.info > a.artist.ellipsis').text


    doc = {
        'rank':rank,
        'title':title,
        'artist':artist
     }

    db.genie.insert_one(doc)


