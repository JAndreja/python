import requests

url ="https://icanhazdadjoke.com/"

resposne = requests.get(url, headers={"Accept": "text/plain"})
resposne1 = requests.get(url, headers={"Accept": "application/json"})
print(resposne.text)
print(resposne1.text)
print(resposne1.json())

data = resposne1.json()

print(type(data))

print(f" The joke is: {data['joke'].upper()}")