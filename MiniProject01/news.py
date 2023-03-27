from bs4 import BeautifulSoup as bs
import requests

query = input('검색할 키워드를 입력하세요: ')
url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='+'%s'%query

response = requests.get(url)
html_text=response.text
soup = bs(html_text, 'html.parser')

#bs4 패키지의 select 함수와 선택자 개념을 이용해서 뉴스기사 제목을 모두 가져온다.
titles = soup.select('a.news_tit')

for i in titles:
    title = i.get_text()
    print(title)

