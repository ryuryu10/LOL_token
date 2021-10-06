from functools import total_ordering
import getpass
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import os.path
import csv

global driver

from webdriver_manager.utils import validate_response

def now_time():
    now = time.localtime()
    return "%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec)

def now_date():
    now = time.localtime()
    return "%04d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday)

User_id = str(input("아이디를 입력하세요 : "))
User_pw = getpass.getpass("비밀번호를 입력하세요 : ")
options = webdriver.ChromeOptions()
options.add_argument("headless")
driver=webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get('https://store.leagueoflegends.co.kr/loot')
driver.implicitly_wait(10)
driver.find_element_by_name('username').send_keys(User_id)
time.sleep(1)
driver.find_element_by_name('password').send_keys(User_pw)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/button').click()
time.sleep(3)
driver.get(driver.current_url)
driver.implicitly_wait(10)
lis=driver.find_elements_by_xpath('//*[@id="lootMaterial"]/ul/li[8]/div/div/span/span/em')
for li in lis:
    print("[{0}] {1}의 패스토큰을 확인하였습니다.".format(now_time(), li.text))

def reload_ses():
    global driver
    driver.quit()
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver=webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get('https://store.leagueoflegends.co.kr/loot')
    driver.implicitly_wait(10)
    driver.find_element_by_name('username').send_keys(User_id)
    time.sleep(1)
    driver.find_element_by_name('password').send_keys(User_pw)
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/button').click()
    time.sleep(3)
    driver.get(driver.current_url)

print("[{0}] 로깅준비중...".format(now_time()))
driver.quit()

while True:
    to_day = now_date()
    if os.path.isfile('data/{0}.csv'.format(now_date())):
        driver.get(driver.current_url)
        driver.implicitly_wait(10)
        lis=driver.find_elements_by_xpath('//*[@id="lootMaterial"]/ul/li[8]/div/div/span/span/em')
        for li in lis:
            token = li.text
        if token >= 0:
            csv_file = open('data/{0}.csv'.format(now_date()),'a',newline='')
            csv_write= csv.writer(csv_file)
            csv_write.writerow([now_date(),now_time(),token])
            csv_file.close()
            time.sleep(600)
        else:
            reload_ses()
        f = open('data/{0}.csv'.format(now_date()),'w')
        f.close()
        reload_ses()