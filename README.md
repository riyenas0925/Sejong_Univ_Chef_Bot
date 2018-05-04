# Sejong Univ Chef Bot

## 세종대학교 학식봇

### 개발자
* 인터페이스 30기 @riyenas0925
* 인터페이스 30기 @2kyung19

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

* python manage.py startapp home

 
## Django 파일 구조

```
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

## ~~pythonanywhere으로 Django 서버 구축하기~~ 
### (현재 AWS 서버 사용중)

> pythonanywhere.com은 손쉽게 Django 서버를 만들수 있다는 장점이 있었지만 무료계정은 외부 사이트에 접속을 못한다는 단점이 있어서 ㅠ AWS서버를 이용하기로 했습니다.

    $ git clone https://github.com/riyenas0925/my-first-blog.git
> git clone 명령어를 이용해 가져오기
> 
    $ tree my-first-blog
    my-first-blog/
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
>
    $ cd my-first-blog
> my-first-blog 폴더로 이동
>
    $ virtualenv --python=python3.6 myvenv
> 가상머신 설치
>
    Running virtualenv with interpreter /usr/bin/python3.6
    [...]
    Installing setuptools, pip...done.

    $ source myvenv/bin/activate

    (myvenv) $  pip install django~=1.11.0
> Django 설치
>
    Collecting django
    [...]
    Successfully installed django-1.11.3

> pythonanywhere web 설정
> 
    Code:
    What your site is running.

    Source code:
    /home/riyenas0925/my-first-blog/ChefBot

    Go to directory
    Working directory:
    /home/riyenas0925/my-first-blog

    Go to directory
    WSGI configuration file:/var/www/riyenas0925_pythonanywhere_com_wsgi.py
    Python version:3.6

## AWS Django 서버 구축하기

> 인스턴스 생성과 접속은 아래글 https://programmers.co.kr/learn/courses/6/lessons/629을 참고 하였습니다.

1. Git, Django, bs4 설치
>
    $ sudo apt-get update
    $ sudo apt-get install git
    $ sudo apt-get install python3-pip
    $ sudo pip3 install django
    $ sudo pip3 install bs4

2. Git에서 리포지토리 가져오기
>
    $ git clone <git 주소>
    $ manage.py가 있는 디렉토리로 이동
    $ python3 manage.py runserver 0.0.0.0:8000

3. 브라우저 접속
>
    브라우저에서 EC2 - Running instances - Public DNS뒤에 :8000붙인 주소로 접속