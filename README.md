
# League Of Legends Pass Token Logger   ![](https://img.shields.io/badge/README%20Language-kor-blue?style=flat-square)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3766AB?style=flat-square&logo=Python&logoColor=white"/></a>
  <img src="https://img.shields.io/badge/Selenium-43B02A?style=flat-square&logo=Selenium&logoColor=white"/></a>
</p>

리그오브레전드의 패스 토큰 변화량을 기록할수 있는 프로그램입니다.

##  목차

- 제작하게된 계기
- 설치방법
- 사용법

## 제작하게된 계기

리그오브레전드라는 게임의 패스를 구매하고 게임을 플레이하면 <br>얻는 토큰의 증가량을 그래프로 표시해보고 싶었습니다.<br>
그래서 시간별로 토큰의 개수를 측정하여 기록해주는 프로그램을 제작하였습니다.

## 설치 방법

1. [이곳](https://github.com/ryuryu10/LOL_token/archive/refs/heads/main.zip)을 눌러 ZIP파일을 다운로드하세요.
2. main.py를 실행하세요.
```
python main.py
```

### 필요한 라이브러리
#### main.py를 실행하기전 사전에 아래 라이브러리들이 설치되있어야합니다.
```
python-opencv
selenium

최신버전을 설치하는것을 권장합니다.
```

## 사용법
1. 필요한 라이브러리에 있는 라이브러리를 설치합니다.
2. python main.py를 터미널에서 실행합니다.
3. 리그오브레전드계정의 아이디, 비밀번호를 입력합니다.
4. 기다립니다.

./data/ 폴더안에 날짜별로 .csv형태로 기록됩니다.
