from bs4 import BeautifulSoup
import chromedriver_autoinstaller
from selenium import webdriver
from time import sleep
import os
import sys

chrome_ver = chromedriver_autoinstaller.get_chrome_version() #크롬드라이버 자동화용
print(chrome_ver)
chromedriver_autoinstaller.install(True)
chromedriver_path = f'./{chrome_ver.split(".")[0]}/chromedriver.exe'
driver = webdriver.Chrome()

url = 'https://www.kw.ac.kr/ko'

driver.get(url)
driver.implicitly_wait(5)
sleep(3)

html = driver.page_source

soup = BeautifulSoup(html, 'lxml')

notice = soup.select('#jwxe_main_content > div:nth-child(4) > section > section > div > div > div.tab_box.on > div.tab_content > ul > li > a')
dates = soup.select('#jwxe_main_content > div:nth-child(4) > section > section > div > div > div.tab_box.on > div.tab_content > ul > li > span')
for i in range(len(notice)):
    notice[i] = notice[i].get_text('\n') + '\r\r'
for i in range(len(dates)):
    dates[i] = dates[i].get_text('\n') + '\r\r'


if os.path.exists('notice.json'):
    os.remove('notice.json')

notice_fp = open('notice.json', 'w', encoding='utf-8')

for i in range(len(notice)):
    notice_fp.writelines(notice[i])
    notice_fp.writelines(dates[i])


driver.get('https://www.kw.ac.kr/ko/life/facility11.jsp')
driver.implicitly_wait(5)
sleep(3)

html = driver.page_source

soup = BeautifulSoup(html, 'lxml')

meal = soup.select('pre')
nowDay = soup.select('#kw_content_w > div.major-contents-box > div > section > div > table > thead > tr > th')


for i in range(len(meal)):
    meal[i] = meal[i].get_text('\n') + '\r\r'
for i in range(len(nowDay)):
    nowDay[i] = nowDay[i].get_text('\n') + '\r\r'

print(nowDay)

if os.path.exists('meal.json'):
    os.remove('meal.json')

notice_fp = open('meal.json', 'w', encoding='utf-8')
for i in range(len(meal)):
    notice_fp.writelines(nowDay[i+1])
    notice_fp.writelines(meal[i])
notice_fp.close()

driver.close()