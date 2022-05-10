import requests

url = "localhost:8000/api/location/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)