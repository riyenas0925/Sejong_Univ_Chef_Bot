from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
import urllib.request
import json
import datetime


def keyboard(request):
    return JsonResponse({
        "message": {
            "text": "무엇이 알고 싶다냥?\n<!--명령어-->*\n*우정당\n*군자관\n*학생회관\n*미세먼지\n*날씨\n*지하철\n"
        },
        "keyboard": {
            "type" : "text"
        }
    })

@csrf_exempt
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content'] #버튼 항목중 무엇을 눌렀는가
    
    def get_menu(place):#변수return_Str를 써야하므로 함수message 안에 같이 넣어줌
        repeat="✧.◟(ˊᗨˋ)◞.✧\n" + date_s(return_str) + return_str + ' 메뉴다냥\n\n'+"---------------\n"
        #repeat == 반복스트링
        if place=='학생회관':
            return repeat+h_menu()

        elif place=='군자관':
            return repeat+g_menu()
            #군자 파싱 함수 만들면 뒤에 이어주면 됨

        elif place=='우정당':
            return repeat+"(ง˙∇˙)ว\n아직 준비 중..."
        else:
            return "٩(๑`^´๑)۶\n잘못입력했다냥!\n다시 입력하라냥!" #사용자입력오류

    return JsonResponse({ #return 밑에는 공통어
        "message": {
            "text": get_menu(return_str)
        },
        "keyboard": {
            "type" : "buttons",
            "buttons" : ["학생회관","군자관","우정당","입력오류테스트"]
        }
    })

'''
def delete(response):

def friend(response):
'''
def date_s(place): #학생회관 클릭 -> 요일 출력 //이 외-> 출력x
    return_date = datetime.datetime.now().strftime("%m월 %d일 ")
    if place=='학생회관':
        return return_date +"\n"
    else:
        return ""

def h_menu():

    req = urllib.request.Request("http://m.sejong.ac.kr/front/cafeteria.do", headers={'User-Agent': 'Mozilla/5.0'})
    con = urllib.request.urlopen(req)
    text = con.read().decode("utf8")

    soup = BeautifulSoup(text, 'html.parser')

    menu = soup.find_all('div',{'class':'th'})
    price = soup.find_all('div',{'class':'td price'})


    ##리스트 menu와 price에 쓰레기값 제거
    for n in menu:
        i = menu.index(n)
        menu[i]= n.get_text()

    for n in price:
        i = price.index(n)
        price[i]= n.get_text()

    foodlist=""

    for i in range(0,len(menu)):
        foodlist += menu[i] + "  " + price[i] + "\n"

    return foodlist

def g_menu():

    req = urllib.request.Request("http://m.sejong.ac.kr/front/cafeteria.do?type1=3", headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    text = response.read().decode("utf8")

    soup = BeautifulSoup(text, 'html.parser')

    day = soup.find_all("th",{'rowspan':'2'})
    menu = soup.find_all('div',{'class':'td'})

    def time(k):
        if k % 2 == 0:
            return '<중식>'

        else:
            return '<석식>'

    ##리스트 menu와 price에 쓰레기값 제거
    for n in day:
        i = day.index(n)
        day[i]= n.get_text().replace("\n","")


    for n in menu:
        i = menu.index(n)
        menu[i]= n.get_text().replace("\t","").replace("\r","").replace("\n\n\n"," ").replace("\n\n"," ").replace("\n"," ").replace(" ","\n").replace("\n\n\n\n\n\n\n\n\n\n\n\n\n\n","")

    foodlist=""
    cnt = 0

    for i in range(0,12):
        if i % 2 == 0:
            foodlist += day[cnt] + '\n\n' + time(i) + menu[i]
            cnt += 1

        else:
            foodlist += '\n' + time(i) + menu[i] + '\n---------------\n\n'

    return foodlist