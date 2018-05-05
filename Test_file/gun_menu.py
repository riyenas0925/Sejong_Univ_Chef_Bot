from bs4 import BeautifulSoup
import urllib.request

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

            temp += day[cnt] + '\n\n' + time(i) + menu[i]
            cnt += 1

        else:
            temp += '\n' + time(i) + menu[i] + '\n---------------\n\n'

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


print(g_menu("군자관"))