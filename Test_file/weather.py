import requests
import json

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

print(weather())