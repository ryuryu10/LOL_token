import getpass
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

User_id = str(input("아이디를 입력하세요 : "))
User_pw = getpass.getpass("비밀번호를 입력하세요 : ")

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver=webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get('https://store.leagueoflegends.co.kr/loot')
driver.implicitly_wait(10)
driver.find_element_by_name('username').send_keys(User_id)
time.sleep(0.3)
driver.find_element_by_name('password').send_keys(User_pw)
time.sleep(0.3)
driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/button').click()
driver.implicitly_wait(10)
driver.get(driver.current_url)
driver.implicitly_wait(10)
lis=driver.find_elements_by_xpath('//*[@id="lootMaterial"]/ul/li[8]/div/div/span/span/em')
print(lis)
for li in lis:
    print(li)
    print(li.text)
driver.quit()