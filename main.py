import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
User_id = str(input("아이디를 입력하세요 : "))
User_pw = getpass.getpass("비밀번호를 입력하세요 : ")

try:
    driver.get('https://store.leagueoflegends.co.kr/loot')
    # driver.find_element_by_name('id').send_keys('아이디') # "아이디라는 값을 보내준다"
    driver.find_element_by_name('username').send_keys(User_id)
    driver.find_element_by_name('password').send_keys(User_pw)
    print(User_id, User_pw)
    driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/button').click()
    driver.get(driver.current_url)
    lis=driver.find_elements_by_xpath('//*[@id="lootMaterial"]/ul/li[8]/div/div/span/span/em') #xpath얻는법 본문에서 설명
    for li in lis:
        print(li.text)  
    input()
except Exception as e:
    print(e)
finally:
    driver.quit()
