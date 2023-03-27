import urllib.request
from urllib import parse
from bs4 import BeautifulSoup
import ssl
context = ssl._create_unverified_context()

search = input("검색어 : ")
url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
newUrl = url+parse.quote_plus(search)

html = urllib.request.urlopen(newUrl,context=context).read()
soup = BeautifulSoup(html,'html.parser')
imgs = soup.find_all('img')
n = 1
for i in imgs:
    if n <= 10:
        src = i.get('src')
        url = src
        savename = str(n)+'.jpg'
        urllib.request.urlretrieve(url, savename)
        n += 1
        print (src)

