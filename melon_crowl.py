from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('-headless')

UserAgent = 'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57'
options.add_argument('user-agent='+UserAgent)

# 드라이브 설정(자동 다운로드 및 대기)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(10)
driver.get(url='https://www.melon.com/')

driver.find_element(By.XPATH, '//*[@id="gnb_menu"]/ul[1]/li[1]/a/span[2]').click()
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="gnb_menu"]/ul[1]/li[1]/div/ul/li[2]/a/span').click()
time.sleep(2)

html = driver.page_source
soup = bs(html, 'html.parser')

songs = soup.select('tbody > tr')

song_list=[]

for song in songs :
    title = song.find('div', class_='ellipsis rank01').text.strip().replace('\n','')
    artist = song.find('div',class_='ellipsis rank02').text.strip().replace('\n','')
#     print(title)
#     print(artist)

song_list.append([title,artist])

df = pd.DataFrame(song_list, columns=['곡명','아티스트'])

df.to_excel('./MELON_100.xlsx', encoding='utf-8', index=False)
