from bs4 import BeautifulSoup
import urllib.request
import json
import datetime
import requests

def get_url(address):
        req = urllib.request.Request(address, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(address)
        text = response.read().decode("utf8")

        return text
    
def notice():
    text = get_url("http://board.sejong.ac.kr/boardlist.do?bbsConfigFK=333")
    soup = BeautifulSoup(text, 'html.parser')
    txt = soup.find_all('a')
    
    html = []
    for i in range(0,5):
        ext = txt[i].get('href').replace("/viewcount.do?rtnUrl=", "").replace('^', '&')
        html.append(ext)

    def notice_main():
        def tag(tag):
            list = all_infor[0].find_all('td', {'class':tag})
            str = list[0].get_text().replace("\r","").replace("\t","")
            return str
        
        string = []
        for i in range(0,5):
            address = "http://board.sejong.ac.kr" + html[i]
            text = get_url(address)
            soup = BeautifulSoup(text, 'html.parser')
            all_infor = soup.find_all('thead')
            
            subject = tag('subject-value')
            writer = tag('writer')
            date = tag('date')

            string.append(subject+"\n"+writer+"\n"+date+"\n\n")
        
        iflist=""
        num=["(1) ","(2) ","(3) ","(4) ","(5) "]

        for i in range(0,5):
            iflist += num[i] + string[i]
        
        return iflist
    
    return notice_main()

text = notice()
print(text)
