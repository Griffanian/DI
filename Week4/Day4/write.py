import requests

responce=requests.get("http://api.open-notify.org/iss-now.json")
data=responce.json()
print(data)