import getpass
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
User_id = str(input("아이디를 입력하세요 : "))
User_pw = getpass.getpass("비밀번호를 입력하세요 : ")

try:
    driver.get('https://store.leagueoflegends.co.kr/loot')
    driver.find_element_by_name('username').send_keys(User_id)
    time.sleep(1)
    driver.find_element_by_name('password').send_keys(User_pw)
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/button').click()
    time.sleep(3)
    driver.get(driver.current_url)
    time.sleep(3)
    lis=driver.find_elements_by_xpath('//*[@id="lootMaterial"]/ul/li[8]/div/div/span/span/em')
    for li in lis:
        print(li.text)
except Exception as e:
    print(e)
finally:
    driver.quit()
