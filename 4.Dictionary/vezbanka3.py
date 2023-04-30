person = {
    "name" : "Andreja",
    "surname" : "Jovanovski",
    "age" : "47",
    "birthyear": "1976"
}
print(person)

person1 = dict( name = "Radica",
                surname= "Jovanovski",
                age = "43",
                 birthyear = "1980" )
print(person1)

only_name = person["name"]
print(only_name[0].upper())
print(person["name"])
print(person1["surname"])

print(f"{person['name'][0].upper()}{person['surname'][0].upper()} roden {person['birthyear']} ima {person['age']}")

for k,v in person.items():
    print(f"{k}:{v}")

for k in person.keys():
    print(k)

for v in person.values():
    print(v)

print(person.get('name'))