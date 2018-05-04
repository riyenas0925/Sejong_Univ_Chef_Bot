import random
from bs4 import BeautifulSoup
import urllib.request
import json

req = urllib.request.Request("http://m.sejong.ac.kr/front/cafeteria.do?type1=2", headers={'User-Agent': 'Mozilla/5.0'})
con = urllib.request.urlopen(req)
text = con.read().decode("utf8")

soup = BeautifulSoup(text, 'html.parser')


mon = soup.find_all('tr',{'class':'seq-01'})
tue = soup.find_all('tr',{'class':'seq-02'})
wed = soup.find_all('tr',{'class':'seq-03'})
thu = soup.find_all('tr',{'class':'seq-04'})
fri = soup.find_all('tr',{'class':'seq-05'})
sat = soup.find_all('tr',{'class':'seq-06'})

day = [mon,tue,wed,thu,fri,sat]
food = []

for i in day:
    for j in i:
        foodname = j.find_all('div',{'class':'td'})
        food.append(foodname)

for i in food:
    j = food.index(i)
    food[j]=i.get_text()

#food
#0~4 월 5~9 화 10~14 수 15~19 목 20~24 금 25~29 토

#시작 5*i
#프리미엄 +0 일품+1 양식+2 한식+3 분식+4

#text만 뽑으면되는데..시볼
