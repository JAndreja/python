import requests
from random import choice

url ="https://icanhazdadjoke.com/search"
user_input = input("Let me tell you a joke! Give me a topic: ")

res = requests.get(
    url,
    headers={"Accept":"application/json"},
    params={"term": user_input}
).json()

num_jokes = res['total_jokes']
results = res['results']
if num_jokes > 1:
    print(f"There is a {num_jokes} jokes about {user_input}. Here's one:\n", 
          choice(results)['joke'])
elif num_jokes == 1:
    print(f"There is only one joke , and the joke is: {results[0]['joke'].upper()}")
else:
    print(f"There is now joke with your term: {user_input}")