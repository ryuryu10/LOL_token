from functools import total_ordering
import getpass
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import os.path
import os
import csv
import cv2
import platform 

if platform.system() == 'Darwin':
    CCMD = 'clear'
else:
    CCMD = "cls"

global driver

from webdriver_manager.utils import validate_response

def now_time():
    now = time.localtime()
    return "%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec)

def now_date():
    now = time.localtime()
    return "%04d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday)

def LOG(message):
    print('[{0} {1}] {2}'.format(now_date(), now_time(), message))

os.system(CCMD)
LOG("---< LOL Token Logger >---")
User_id = str(input("아이디를 입력하세요 : "))
User_pw = getpass.getpass("비밀번호를 입력하세요 : ")
LOG('프로세스를 시작하는중...')
options = webdriver.ChromeOptions()
options.add_argument("headless")
driver=webdriver.Chrome(ChromeDriverManager().install(), options=options)
os.system(CCMD)
LOG('프로세스가 시작되었습니다.')
driver.get('https://store.leagueoflegends.co.kr/loot')
driver.implicitly_wait(10)
LOG('로그인중. 잠시만 기다려주세요.')
driver.find_element_by_name('username').send_keys(User_id)
time.sleep(1)
LOG('로그인중.. 잠시만 기다려주세요.')
driver.find_element_by_name('password').send_keys(User_pw)
time.sleep(1)
LOG('로그인중... 잠시만 기다려주세요.')
driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/button').click()
time.sleep(3)
LOG('토큰 정보를 불러오는중...')
driver.get(driver.current_url)
driver.implicitly_wait(10)
lis=driver.find_elements_by_xpath('//*[@id="lootMaterial"]/ul/li[8]/div/div/span/span/em')
for li in lis:
    LOG('{0}개의 패스토큰을 발견하였습니다.'.format(li.text))

def reload_ses():
    LOG('새션을 새로고침중...')
    global driver
    LOG('이전 새션정보 삭제중...')
    driver.quit()
    LOG('프로세스를 새로 시작하는중...')
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver=webdriver.Chrome(ChromeDriverManager().install(), options=options)
    LOG('로그인중... 약간의 시간이 소요됩니다.')
    driver.get('https://store.leagueoflegends.co.kr/loot')
    driver.implicitly_wait(10)
    driver.find_element_by_name('username').send_keys(User_id)
    time.sleep(1)
    driver.find_element_by_name('password').send_keys(User_pw)
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/button').click()
    time.sleep(3)
    driver.get(driver.current_url)
    LOG('새션 새로고침이 완료되었습니다.')

LOG('로깅을 시작합니다...')
try:
    while True:
        if os.path.isfile('data/{0}.csv'.format(now_date())):
            LOG('토큰 정보를 불러오는중...')
            driver.get(driver.current_url)
            driver.implicitly_wait(10)
            lis=driver.find_elements_by_xpath('//*[@id="lootMaterial"]/ul/li[8]/div/div/span/span/em')
            for li in lis:
                token = li.text
            if int(token) >= 0:
                LOG('{0}개의 값을 입력하는중...'.format(token))
                csv_file = open('data/{0}.csv'.format(now_date()),'a',newline='')
                csv_write= csv.writer(csv_file)
                csv_write.writerow([now_date(),now_time(),token])
                csv_file.close()
                LOG('다음 기록까지 10분 남았습니다.')
                time.sleep(600)
                
            else:
                reload_ses()
        else:
            LOG('날짜가 변경되었거나, 기존 파일을 찾을수 없습니다.')
            LOG('파일을 새로 생성하고 새션을 새로고침합니다.')
            f = open('data/{0}.csv'.format(now_date()),'w')
            f.close()
            reload_ses()
except KeyboardInterrupt:
    driver.quit()