import requests
import json
import urllib.request

params = {
    "ServiceKey" : "%2B4klnL3ynce%2FXUyXXH0E%2B5x0WMdfRMUnOr8TS7qzltpflaw11MRbtGsat%2FnipcomUkQmirZMq1QBAPkohvC2vw%3D%3D",
    'numOfRows' : '10',
    'pageSize' : '10',
    'pageNo' : '1',
    'startPage' : '1',
    'stationName' : '종로구',
    'dataTerm' : 'DAILY',
    'ver' : '1.3'
}

req = requests.get("http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst", params=params)

print(req)

# numOfRows=10&pageSize=10&pageNo=1&startPage=1&stationName=%EC%A2%85%EB%A1%9C%EA%B5%AC&dataTerm=DAILY&ver=1.3