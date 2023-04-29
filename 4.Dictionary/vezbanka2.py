person = {
    "name" : "Andreja",
    "surname" : "Jovanovski",
    "age" : "47",
    "birthyear": "1976"
}
print(person)

person1 =  dict ( name = "Radica",
                  surname = "Jovanovski",
                  age = "43",
                  birthyear = "1980" )
print(person1)


person2 = dict ([('name','Kaja'),
                 ('surname','Jovanovski'),
                 ('age', '11'),
                 ( 'birthyear', '2011')])
print(person2)


print(f"{person['name']} {person['surname']}")
print(person["name"])
print(person1["age"])
print(person2["birthyear"])

for val in person.values():
    print(val)

for key in person.keys():
    print(key)

for key, val in person.items():
    #print(keys + ":" + val)
     print(f"{key}:{val}")


new_user = {}.fromkeys(['name', 'score', 'email'], "unknown")
print(new_user)



from random import choice 
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) 
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

if food in bakery_stock:
    print(f"{food}: {bakery_stock[food]} left")
else:
    print("We don't make that")
    
