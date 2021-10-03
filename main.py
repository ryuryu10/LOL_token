from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())

def login_mode(mode):
    if mode == 'saved':
        login = {
            "id" : "id",
            "pw" : "pw"
        }
    elif mode == 'input':
        pass

try:
    driver.get('https://store.leagueoflegends.co.kr/loot') #크롤링 하고싶은 사이트 입력
    elem=driver.find_element_by_id('container')  #id얻는법 본문에서 설명
    lis=elem.find_elements_by_xpath('./div[5]/div[2]/div[2]/div[1]/h3') #xpath얻는법 본문에서 설명
    for li in lis:
        print(li.text)  
    input()
except Exception as e:
    print(e)
finally:
    driver.quit()
