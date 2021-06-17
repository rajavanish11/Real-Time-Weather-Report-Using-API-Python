import requests
import os

location=input("Enter the city name:")

key=os.environ['api_key']

api_url="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+key

request=requests.get(api_url)

data=request.json()

if data['cod']=='404':
    print("Invalid city {}, Please check your city name.".format(location))

else:
    temp_city=((data['main']['temp'])-273.15)
    weather_desc=data['weather'][0]['description']
    humidity=data['main']['humidity']
    wind_speed=data['wind']['speed']


    print("---------------------------------------------------")
    print("Weather Stats for {}".format(location.upper()))
    print("---------------------------------------------------")

    print("Current Temperature is: {:.2f} deg C".format(temp_city))
    print("Current Weather Description: {}".format(weather_desc))
    print("Humidity: {}%".format(humidity))
    print("Wind Speed is:",wind_speed,"kmph")

