import requests
import json
from constants import API_KEY as appid, ID as id

# API FOURSQUARE не позволяет авторизоваться и получить API KEY. Для выполнения проекта выбрал https://openweathermap.org/api
# сначала получим координаты для места
city = input('Введите наименование города: ')
url_coordinates = 'http://api.openweathermap.org/geo/1.0/direct'
params_coordinates = {
    'q': city,
    'limit': 1,
    'appid': appid
}
coordinates_city = requests.get(url=url_coordinates, params=params_coordinates)
print(coordinates_city.json())
lon = round(coordinates_city.json()[0]['lon'], 2)
lat = round(coordinates_city.json()[0]['lat'], 2)


url = 'https://api.openweathermap.org/data/2.5/weather'
params = {
    'lat': lat,
    'lon': lon,
    'appid': appid
}
data_weather = requests.get(url=url, params=params)
data_weather_json = data_weather.json()
temp = data_weather_json.get('main').get('temp')
humidity = data_weather_json.get('main').get('humidity')
visibility = data_weather_json.get('visibility')

print(f'В городе {city} температура {temp}, влажность {humidity}, видимость {visibility} метров')