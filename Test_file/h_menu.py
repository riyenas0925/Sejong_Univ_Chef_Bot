from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.Request("http://m.sejong.ac.kr/front/cafeteria.do", headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
text = response.read().decode("utf8")

'''
html = urllib.request.urlopen("http://m.sejong.ac.kr/front/cafeteria.do")
text = html.read().decode("utf8")
'''
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
    foodlist += menu[i] +""+price[i]+"\n"

print(foodlist)