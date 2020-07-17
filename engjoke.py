import json
import requests
response = requests.get("https://joke3.p.rapidapi.com/v1/joke",
  headers={
    "X-RapidAPI-Host": "joke3.p.rapidapi.com",
    "X-RapidAPI-Key": " ",
    "Content-Type": "application/json"
  },
  params=("{\"content\":\"A joke here\",\"nsfw\":\"false\"}")
)

a=response.text
a=json.loads(a)
joke=a['content']
