import getpass
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def now_time():
    now = time.localtime()
    return "%04d/%02d/%02d %02d:%02d:%02d " % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

print("[{0}] LOL Token Logger".format(now_time()))
print("[{0}] 로그인 정보를 입력해주세요.".format(now_time()))
User_id = str(input("아이디를 입력하세요 : "))
User_pw = getpass.getpass("비밀번호를 입력하세요 : ")
print("[{0}] 프로세스 시작중...".format(now_time()))
options = webdriver.ChromeOptions()
options.add_argument("headless")
driver=webdriver.Chrome(ChromeDriverManager().install(), options=options)
print("[{0}] 사이트 접속중...".format(now_time()))
driver.get('https://store.leagueoflegends.co.kr/loot')
driver.implicitly_wait(10)
print("[{0}] 로그인중... 1/3".format(now_time()))
driver.find_element_by_name('username').send_keys(User_id)
time.sleep(1)
print("[{0}] 로그인중... 2/3".format(now_time()))
driver.find_element_by_name('password').send_keys(User_pw)
time.sleep(1)
print("[{0}] 로그인중... 3/3".format(now_time()))
driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/button').click()
time.sleep(3)
print("[{0}] 계정 정보를 불러오는중... 잠시만 기다려주세요.".format(now_time()))
driver.get(driver.current_url)
driver.implicitly_wait(10)
lis=driver.find_elements_by_xpath('//*[@id="lootMaterial"]/ul/li[8]/div/div/span/span/em')
for li in lis:
    print("[{0}] {1}의 패스토큰을 확인하였습니다.".format(now_time(), li.text))

print("[{0}] 로깅준비중...".format(now_time()))

while True:
    print("[{0}] 계정 정보를 새로 불러오는중...".format(now_time()))
    driver.get(driver.current_url)
    driver.implicitly_wait(10)
    lis=driver.find_elements_by_xpath('//*[@id="lootMaterial"]/ul/li[8]/div/div/span/span/em')
    print("[{0}] 정보를 추가하는중...".format(now_time()))
    f = open("log.txt",'a')
    for li in lis:
        print("[{0}] {1}의 패스토큰을 확인하였습니다.".format(now_time(), li.text))
        data = now_time() + li.text + '\n'
        f.write(data)
    f.close()
    print("[{0}] 대기중... 10분남음".format(now_time()))
    time.sleep(60)
    print("[{0}] 대기중... 9분남음".format(now_time()))
    time.sleep(60)
    print("[{0}] 대기중... 8분남음".format(now_time()))
    time.sleep(60)
    print("[{0}] 대기중... 7분남음".format(now_time()))
    time.sleep(60)
    print("[{0}] 대기중... 6분남음".format(now_time()))
    time.sleep(60)
    print("[{0}] 대기중... 5분남음".format(now_time()))
    time.sleep(60)
    print("[{0}] 대기중... 4분남음".format(now_time()))
    time.sleep(60)
    print("[{0}] 대기중... 3분남음".format(now_time()))
    time.sleep(60)
    print("[{0}] 대기중... 2분남음".format(now_time()))
    time.sleep(60)
    print("[{0}] 대기중... 1분남음".format(now_time()))
    time.sleep(60)
    
    
driver.quit()



