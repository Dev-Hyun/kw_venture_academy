import os
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from urllib.request import urlretrieve

chrome_ver = chromedriver_autoinstaller.get_chrome_version() #크롬드라이버 자동화용
print(chrome_ver)
chromedriver_autoinstaller.install(True)
chromedriver_path = f'./{chrome_ver.split(".")[0]}/chromedriver.exe'

query = input('검색할 키워드를 입력하세요: ')
url = 'https://www.naver.com/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)
search_box = driver.find_element_by_css_selector("input#query")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="lnb"]/div[1]/div/ul/li[2]/a').click()
time.sleep(1)
img_lst = driver.find_elements_by_css_selector("._image._listImage")
image = []
for img in img_lst:
    image.append(img.get_attribute('src'))
path_folder = '/Users/dev_hyun/kw_venture_academy/MiniProject02/cat/cat'
if not os.path.isdir(path_folder):
    os.mkdir(path_folder)
i = 0
n = 1
for link in image:
    if n <= 10:
        i += 1
        urlretrieve(link, path_folder + f'{i}.jpg')
        n += 1
