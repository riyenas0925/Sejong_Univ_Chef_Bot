<h1 align="center">Sejong Univ Chef Bot  :joy_cat: </h1>

![date](https://img.shields.io/badge/Project_Start_Date-2018--05--01-blue)
![user count](https://img.shields.io/badge/User_Count-121-green)

<p align="center">
  <img src="https://user-images.githubusercontent.com/32615702/71518315-929bbd00-28f5-11ea-8270-2ccd38f72422.gif">
</p>

현재 [카카오 API형 스마트 채팅](https://github.com/plusfriend/auto_reply) 이 2018년 12월 3일 카카오 i 오픈빌더 오픈에 따라 중단됨으로서 세종대학교 학식봇인 세종냥이는 2019년 12월 31일 까지 사용하실수 있습니다

<h6 align="center">"그동안 세종냥이를 길러주신 학우분들께 감사의 말씀 올립니다!"</h6>

## 개발자
* [@riyenas0925](https://github.com/riyenas0925) - 세종대학교 학술동아리 인터페이스 30기
* [@2kyung19](https://github.com/2kyung19) - 세종대학교 학술동아리 인터페이스 30기  

## 기능
> ```키워드```로 사용자의 메시지를 이해하기 때문에 오늘 ```날씨``` 어때?, ```군자관``` ```목```요일 메뉴 알려줘 같은 문장도 입력가능 하다냥~

| # | 기능 명 | 기능 | ```키워드``` | 사용예시 |
|:--------:|:--------:|:--------:|:--------:|:--------:|
| 1 | 학식 메뉴 | 학식 메뉴 표시 | ```학생회관```, ```군자관```, ```우정당```, ```요일``` | ```군자관``` ```목```요일 메뉴 알려줘|
| 2 | 미세먼지 | 광진구 미세먼지 표시 | ```미세먼지``` | 오늘의 ```미세먼지``` 알려줘 |
| 3 | 날씨 | 광진구 날씨 표시  | ```날씨``` | 오늘의 ```날씨``` 알려줘 |
| 4 | 공지사항 | 최근 10개 공지 표시 | ```공지사항``` | 새로운 ```공지사항``` 알려줘 |

## 기술 스택
```
Deploy Server : AWS EC2  
Language : Python3  
Web Framework : Django  
Version Control : git  
```

## 작동 흐름
![1542113245976](https://user-images.githubusercontent.com/32615702/71469976-17aba700-280e-11ea-8c38-49e3244f40a4.jpg)

## AWS에서 Django 서버 구축하기

1. Git, Django, bs4 설치
```bash
$ sudo apt-get update
$ sudo apt-get install git
$ sudo apt-get install python3-pip
$ sudo pip3 install django~=1.11.0
$ sudo pip3 install bs4
```

2. Git에서 리포지토리 가져오기
```bash
$ git clone <git 주소>
$ manage.py가 있는 디렉토리로 이동
$ python3 manage.py runserver 0.0.0.0:8000
```

3. SSL 접속 종료와 상관없이 서버 계속 켜두기
```bash
$ nohup python3 manage.py runserver 0.0.0.0:8000 &
```

4. 브라우저 접속
```bash
브라우저에서 EC2 - Running instances - Public DNS뒤에 :8000붙인 주소로 접속
```

## Sejong Univ Chef Bot 파일 구조

```bash
ChefBot:            //프로젝트 폴더
│  db.sqlite3
│  manage.py
│
├─ChefBot           //프로젝트의 기본적인 설정 폴더
│  │  settings.py   //Django 설정 세팅
│  │  urls.py       //서버에 요청이 들어오면 누가 처리하는지 정하는 부분
│  │  wsgi.py
│  │  __init__.py
│  │
│  └─__pycache__
│
└─home              //app 폴더
    │  admin.py
    │  apps.py
    │  models.py
    │  tests.py
    │  views.py     //Keyboard, Message, delete, friend 함수 View Page
    │  __init__.py
    │
    ├─migrations
    └─__pycache__

```
