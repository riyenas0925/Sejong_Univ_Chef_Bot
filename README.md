# Sejong Univ Chef Bot

## 세종대학교 학식봇

## 장고 설치하기

1. 장고 설치하고 프로젝트 만들기

* pip
    > pip로 파이썬이 설치되어있는지 확인

* pip install django~=1.11.0
    > pip 명령어를 이용해서 django 1.11.0 설치

* D:
    > C에서 D로 디렉토리를 변경한다.

* cd D:\Users\riyenas0925\project\Sejong_Univ_Chef_Bot
    > 프로젝트를 생성하고 싶은 폴더로 이동

* django-admin startproject firstServer
    > firstSever라는 django 프로젝트를 제작

* cd firstServer
    > firstServer 폴더로 이동

* python manage.py runserver
    > django 시작
 
## Django 파일 구조

```
D:.
│  db.sqlite3
│  manage.py
│
├─ChefBot
│  │  settings.py   //Django 설정
│  │  urls.py       //Django 접속 URL 설정
│  │  wsgi.py
│  │  __init__.py
│  │
│  └─__pycache__
│
└─home
    │  admin.py
    │  apps.py
    │  models.py
    │  tests.py
    │  views.py     //Keyboard, Message 함수 View Page
    │  __init__.py
    │
    ├─migrations
    └─__pycache__

```