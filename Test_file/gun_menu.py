from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.Request("http://m.sejong.ac.kr/front/cafeteria.do?type1=3", headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
text = response.read().decode("utf8")

soup = BeautifulSoup(text, 'html.parser')

day = soup.find_all("th",{'rowspan':'2'})
menu = soup.find_all('div',{'class':'td'})

def time(k):
    if k % 2 == 0:
        return '중식'

    else:
        return '석식'

##리스트 menu와 price에 쓰레기값 제거
for n in day:
    i = day.index(n)
    day[i]= n.get_text().replace("\n","")


for n in menu:
    i = menu.index(n)
    menu[i]= n.get_text().replace("\t","").replace("\r","")

foodlist=""
cnt = 0

for i in range(0,12):
    if i % 2 == 0:
        foodlist += '\n-----------\n' + day[cnt] + '\n' + time(i) + '\n' + menu[i] + '\n\n'
        cnt += 1

    else:
        foodlist += time(i) + '\n' + menu[i] + '\n'

print(menu)