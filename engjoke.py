import json
import requests
response = requests.get("https://joke3.p.rapidapi.com/v1/joke",
  headers={
    "X-RapidAPI-Host": "joke3.p.rapidapi.com",
    "X-RapidAPI-Key": "83a77d59f4msh721e0959e3a7c66p12844bjsn3a783262714d",
    "Content-Type": "application/json"
  },
  params=("{\"content\":\"A joke here\",\"nsfw\":\"false\"}")
)

a=response.text
a=json.loads(a)
joke=a['content']