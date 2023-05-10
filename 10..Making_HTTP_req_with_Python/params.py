import requests

url ="https://icanhazdadjoke.com/search"

resposne = requests.get(
    url, 
    headers={"Accept": "application/json"},
    params={"term":"cat", "limit":1})

data = resposne.json()
print(data['results'])

for x in data['results']:
    print(f"The joke is: {x['joke']}")