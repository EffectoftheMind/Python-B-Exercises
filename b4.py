import requests

url = "https://analytics.usa.gov/data/live/realtime.json"

r = requests.get(url)

print(r.json()['data'][0]["active_visitors"])
