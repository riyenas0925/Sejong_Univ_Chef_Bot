import json
import requests
from bs4 import BeautifulSoup

'''
params = {
    'ServiceKey' : 'ServiceKey=%2B4klnL3ynce%2FXUyXXH0E%2B5x0WMdfRMUnOr8TS7qzltpflaw11MRbtGsat%2FnipcomUkQmirZMq1QBAPkohvC2vw%3D%3D',
    'numOfRows' : '1',
    'pageSize' : '1',
    'pageNo' : '1',
    'startPage' : '1',
    'stationNa+me' : '종로구',
    'dataTerm' : 'DAILY',
    'ver' : '1.3',
}

response = requests.get("http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty", params=params)
'''

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

    printdust = '미세먼지(pm10) : ' + pm10value + '㎍/㎥\n' '등급 : ' + grade(pm10grade) + '\npm2.5(초미세먼지) : ' + pm25value + '㎍/㎥\n' + '등급 : ' + grade(pm25grade)
    
    return printdust

print(dust())