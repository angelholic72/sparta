import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/bi/mi/basic.nhn?code=136873',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

image = soup.select_one('meta[property="og:image"]')
print(image['content'])

title = soup.select_one('meta[property="og:title"]')
print(title['content'])

desc = soup.select_one('meta[property="og:description"]')
print(desc['content'])
