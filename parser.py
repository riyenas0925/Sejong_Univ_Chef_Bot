from bs4 import BeautifulSoup
import urllib.request
import json

html = urllib.request.urlopen("http://m.sejong.ac.kr/front/cafeteria.do")
text = html.read().decode("utf8")

soup = BeautifulSoup(text, 'html.parser')

menu = soup.find_all('div',{'class':'th'})
price = soup.find_all('div',{'class':'td price'})

for n in menu:
        print(n.get_text())

for n in price:
       print(n.get_text())        

