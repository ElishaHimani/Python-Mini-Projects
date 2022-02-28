import requests
from pprint import pprint

API_KEY = '2d81d1ad5c9cdc7ecd42ee0dc9fc80da'
city = input("Enter a city: ")
#base_url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+API_KEY
base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+city
weather_data = requests.get(base_url).json()
pprint(weather_data)
