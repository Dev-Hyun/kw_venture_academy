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
url = 'https://www.google.com/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)
search_box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[4]/a').click()
time.sleep(1)
img_lst = driver.find_elements_by_css_selector(".VYkpsb")
image = []
for img in img_lst:
    image.append(img.get_attribute('data-url'))
del image[1::2]
path_folder = '/Users/dev_hyun/kw_venture_academy/MiniProject02/corona/corona'
if not os.path.isdir(path_folder):
    os.mkdir(path_folder)
i = 0
for link in image:
    if link != ' None':
        urlretrieve(link, path_folder + f'{i}.mp4')
    i += 1
