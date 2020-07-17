import requests
from pprint import pprint
response = requests.get("https://community-open-weather-map.p.rapidapi.com/weather?callback=test&id=2172797&units=%22metric%22+or+%22imperial%22&mode=xml%2C+html&q=maharajganj%2CIN",
  headers={
    "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
    "X-RapidAPI-Key": " "
  }
)
import json
a=response.text
print(a)

#print(a["weather"][0]['description'])
