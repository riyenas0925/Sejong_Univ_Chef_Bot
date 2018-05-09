from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
import urllib.request
import json
import datetime
import requests


def keyboard(request):
    return JsonResponse(
        {
            "type" : "text"
        }   
    )

@csrf_exempt
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content'] #버튼 항목중 무엇을 눌렀는가
    
    def get_menu(place):#변수return_Str를 써야하므로 함수message 안에 같이 넣어줌
        repeat="✧.◟(ˊᗨˋ)◞.✧\n" + date_s(return_str) + return_str + ' 메뉴다냥\n'
        end_repeat="\n================="+"\n٩(๑>∀<๑)۶다른 명령어는\n아무말이나 해보라냥~"
        #repeat == 반복스트링

        if place.find('학생회관') != -1:
            return JsonResponse({ #return 밑에는 공통어
                "message": {
                    "text": repeat+h_menu()+end_repeat
                }
            })

        elif place.find('군자관') != -1:
            return JsonResponse({ #return 밑에는 공통어
                "message": {
                    "text": repeat+g_menu(return_str)+end_repeat
                }
            }) 
            #군자 파싱 함수 만들면 뒤에 이어주면 됨

        elif place.find('우정당') != -1:
            return JsonResponse({ #return 밑에는 공통어
                "message": {
                    "text": repeat+u_menu(return_str)+end_repeat
                }
            })
        elif place.find('배고파') != -1:
            return JsonResponse({
                "message": {
                    "text": "(๑˃̵ᴗ˂̵)و "+"\n우리집 밥 진짜 맛있따냥!\n\n학생회관,군자관,우정당\n메뉴를 알려줄 수 있다냥~\n\nex)\n학생회관,군자관,군자관 목,우정당 월"
                }

            })

        elif place.find('날씨') != -1:
            return JsonResponse({ #return 밑에는 공통어
                "message": {
                    "text": '✧*｡٩(ˊᗜˋ*)و✧*｡ \n' + '우리집 날씨다냥\n\n'+ weather()+end_repeat
                }
            })

        elif place.find('미세먼지') != -1:
            
            return JsonResponse({ #return 밑에는 공통어
                "message": {
                    "text": '✧*｡٩(ˊᗜˋ*)و✧*｡ \n' + '우리집 미세먼지다냥\n참고하라냥\n\n'+ dust()+end_repeat
                }
            })

        elif place == '개발자' or place=='집사':
            return JsonResponse({ #return 밑에는 공통어
                "message": {
                    "text": "*ଘ(੭*ˊᵕˋ)੭* ੈ♡‧₊˚\n세종냥이 집사라냥!\n\n" +"세종대학교\n중앙동아리 인터페이스 30기\n-------------------\n전자정보통신공학과\n-------------------\n♡⁺◟강동민◞⁺♡\n  @riyenas0925\n\n"+"-------------------\n바이오산업자원공학과\n-------------------\n✧*｡이경은✧*｡ \n  @2kyung19"+end_repeat
                }
            })

        elif place =='공지' or place=='공지사항':
            return JsonResponse({
                "message":{
                    "text":"⁽⁽◝( ˙ ꒳ ˙ )◜⁾⁾\n세종대학교 공지사항이라냥!\n최근 5개까지만 올려준다냥\n\n"+notice(),
                
                    "message_button": {
                        "label": "세종대학교 공지 바로가기",
                        "url": "http://board.sejong.ac.kr/boardlist.do?bbsConfigFK=333"
                    }
                }
            })

        elif place =='인터페이스' or place == 'interface':
            return JsonResponse({
                "message":{
                    "text":"*ଘ(੭*ˊᵕˋ)੭* ੈ♡‧₊˚\n세종대학교\n컴퓨터 중앙 학술동아리\n인터페이스라냥~\n\nhttps://sejong-interface.github.io/"

                    }
            
            })

        else:
            return JsonResponse({ #return 밑에는 공통어
                "message": {
                    "text": '٩(๑`^´๑)۶\n키워드를 넣어서 물어보라냥~!\n\n-키워드-\n*학생회관\n*군자관\n*우정당\nex)학생회관,군자관 목\n\n -키워드-\n*미세먼지\n*날씨\nex)오늘 날씨 어때?,날씨\n\n-키워드-\n*공지사항\n*개발자'
                }
            })
             #사용자입력오류

    return get_menu(return_str)

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
        foodlist += '\n' + menu[i] + "  " + price[i]

    return '\n' + foodlist

def g_menu(type):
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

    temp=""
    foodlist_day=['','','','','','']
    foodlist_all=''
    cnt = 0

    for i in range(0,12):
        if i % 2 == 0:
            foodlist_day[cnt-1] = temp
            temp=""

            temp += '\n\n' + day[cnt] + '\n\n' + time(i) + menu[i]
            cnt += 1

        else:
            temp += '\n' + time(i) + menu[i] + '\n---------------'

    foodlist_all = foodlist_day[0] + foodlist_day[1] + foodlist_day[2] + foodlist_day[3] + foodlist_day[4]

    if type == '군자관 월':
        return foodlist_day[0]

    elif type == '군자관 화':
        return foodlist_day[1]

    elif type == '군자관 수':
        return foodlist_day[2]

    elif type == '군자관 목':
        return foodlist_day[3]

    elif type == '군자관 금':
        return foodlist_day[4]

    else:
        return foodlist_all
    
def u_menu(type):
    req = urllib.request.Request("http://m.sejong.ac.kr/front/cafeteria.do?type1=2", headers={'User-Agent': 'Mozilla/5.0'})
    con = urllib.request.urlopen(req)
    text = con.read().decode("utf8")

    soup = BeautifulSoup(text, 'html.parser')

    food=[]
    day_d=[]

    def parsing(seq):
        day = soup.find_all('tr',{'class':seq})
        a=day[0].find_all('div',{'class':'th'})
        b = a[0].get_text()
        day_d.append(b)
    
        for n in day:
            day_f=n.find_all('div',{'class':'td'})
    
            a=day_f[0].get_text().replace("\t","").replace("\r","")
            food.append(a)

    parsing("seq-01")
    parsing("seq-02")          
    parsing("seq-03")
    parsing("seq-04")
    parsing("seq-05")
    parsing("seq-06")
    dayday=['우정당 월','우정당 화','우정당 수','우정당 목','우정당 금','우정당 토']
    dayday1=['우정당 월요일','우정당 화요일','우정당 수요일','우정당 목요일','우정당 금요일','우정당 토요일']
    printlist=""
    
    for i in range(0,5):
        if type==dayday[i] or type==dayday1[i]:
            printlist+="-------------\n"+day_d[i]+"\n-------------"+"\n<프리미엄>"+food[5*i]+"\n<일품>"+food[5*i+1]+"\n<양식>"+food[5*i+2]+"\n<한식>"+food[5*i+3]+"\n<분식>"+food[5*i+4]
        #0~4 월 5~9 화 10~14 수 15~19 목 20~24 금 25~29 토
        #프리미엄 +0 일품+1 양식+2 한식+3 분식+4
        #시작 5*i
    
    if printlist=="":
        printlist="\n(*ૂ❛ัᴗ❛ั*ૂ)\n우정당은 요일까지 적어달라냥!\n\nex)우정당 월요일, 우정당 화"

    return printlist


def weather():
    params = {"version": "1", "city":"서울", "county":"광진구","village":"군자동"}
    headers = {"appKey": "ea6c12af-2d3c-4572-a9a9-30d42a9742d4"}
    response = requests.get("https://api2.sktelecom.com/weather/current/minutely", params=params, headers=headers)

    data = json.loads(response.text)

    weather = data["weather"]["minutely"]
    sky = weather[0]["sky"]["name"]
    wind = weather[0]["wind"]["wspd"]
    temp = weather[0]["temperature"]["tc"]
    time = weather[0]["timeObservation"]

    printweather = '하늘 : ' + sky + '\n' + '온도 : ' + temp + 'C\n' + '풍속 : ' + wind + 'm/s'

    return printweather

def dust():
    ServiceKey = "ServiceKey=%2B4klnL3ynce%2FXUyXXH0E%2B5x0WMdfRMUnOr8TS7qzltpflaw11MRbtGsat%2FnipcomUkQmirZMq1QBAPkohvC2vw%3D%3D"

    response = requests.get("http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?numOfRows=1&pageSize=1&pageNo=1&startPage=1&stationName=%EC%A2%85%EB%A1%9C%EA%B5%AC&dataTerm=DAILY&ver=1.3&" + ServiceKey)

    soup = BeautifulSoup(response.text, 'html.parser')

    pm10value = soup.find('pm10value').get_text()
    pm10grade = soup.find('pm10grade').get_text()

    pm25value = soup.find('pm25value').get_text()
    pm25grade = soup.find('pm25grade').get_text()

    def grade(k):
        if k == '1':
            return '좋음'
        
        elif k == '2':
            return '보통'

        elif k == '3':
            return '나쁨'

        else:
            return '매우나쁨'

    printdust = '미세먼지(pm10) : ' + pm10value + '㎍/㎥\n' '등급 : ' + grade(pm10grade) + '\n초미세먼지(pm2.5) : ' + pm25value + '㎍/㎥\n' + '등급 : ' + grade(pm25grade)
    
    return printdust

def notice():
    req = urllib.request.Request("http://board.sejong.ac.kr/boardlist.do?bbsConfigFK=333", headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    text = response.read().decode("utf8")

    soup = BeautifulSoup(text, 'html.parser')

    all_infor=soup.find_all('tbody')
    
    subject = all_infor[0].find_all('td',{'class':"subject"})
    writer=all_infor[0].find_all('td',{'class':"writer"})
    date=all_infor[0].find_all('td',{'class':"date"})

    s_str=[]
    w_str=[]
    d_str=[]
    for i in range(0,5):
        n = subject[i].get_text().replace("\r","").replace("\t","").replace("\n","")
        s_str.append(n)
        m = writer[i].get_text().replace("\r","").replace("\t","")
        w_str.append(m)
        l = date[i].get_text().replace("\r","").replace("\t","")
        d_str.append(l)

    iflist=""

    num=["(1) ","(2) ","(3) ","(4) ","(5) "]
    for i in range(0,len(s_str)):
        iflist += num[i]+s_str[i] + "\n" + w_str[i]+"\n"+d_str[i]+"\n\n"

    return iflist