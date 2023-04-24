# d ={key:value,
#     key:value,
#     key:value}


person = {
    # key:  value
    "name":"Andreja",
    "surname":"Jovanovski",
    "age": "44",
    "own_dog": False,
     44: "favorite number"
}
print("Print dictionary:")
print()
print(person)
print("------------------------")

# use of dict function
person1 = dict( name="Radica",
              surname="Jovanovski",
              age= "40",
              own_dog= False)
person2 = dict ([('name','Kaja'),
                 ('surname','Jovanovski'),
                 ('age', 11)] )
print("Print dictionary using dict function:")
print()
print(person)
print(person2)
print("------------------------")

# accessing individual values
print("Accessing individual values:")
print()
print(person["name"])
print("**string concatenation method:")
print(person["name"] + " " + person["surname"])
print("** f-string method:")
print(f"{person['name']} {person['surname']}")
print(person1["name"])
print("------------------------")

# accessing all values
print("Accessing all values:")
print()
for val in person.values():
    print(val)
print("------------------------")

# accessing all keys
print("Accessing all keys:")
print()
for key in person.keys():
    print(key)
print("------------------------")

# accessing all values and keys
print("Accessing all values and keys:")
print()
for key,value in person.items():
    print(f"{key}:{value}")
print("------------------------")

#check if a value exist in dictionary
print()
print(f"'Andreja' value exist in dictionary: {'Andreja' in person.values()}")
print(f"'43' value exist in dictionary: {'43' in person.values()}")
print("------------------------")
#check if a key exist in dictionary
print()
print(f"'name' key exist in dictionary: {'name' in person.keys()}")
print(f"'test' key exist in dictionary: {'test' in person}")
print("------------------------")

# Dictionary methods
print("** DICTIONARY METHODS **")
print()
# Clear, Copy , Fromkeys , Get , Pop , Popitem , Update
print("CLEAR:")
d = dict( a=1 , b=2 , c=3)
print(f"Dictionary before clearing: {d}")
d.clear()
print(f"Dictionary after clearing: {d}")
print()
print("COPY:")
d = dict( a=1 , b=2 , c=3)
print(f"Dictionary before copying: {d}")
clone=d.copy()
print(f"Dictionary after copying in new variable: {clone}")
print()
# Creates key-value pairs from comma separated values
print("FROMKEYS:")
dict1={}.fromkeys("a","b")
print(dict1)
dict2={}.fromkeys(["email","password"], 'unknown')
print(dict2)
dict3={}.fromkeys("a",[1,2,3,4,5])
print(dict3)
print()
# Retrieves a key in an object and return None instead of a KeyError if the key does not exist
print("GET:")           
d = dict( a=1 , b=2 , c=3)
print(d)
print(f"a:{d.get('a')}")
print()
print("POP:")
print(f"Before removing a key: {d}")
d.pop('a')
print(f"After removing a key: {d}")
print()
print("Removing a random key POPITEM:")
d = dict(a=1,b=2,c=3,d=4,e=5)
print(f"Before random remove: {d}")
d.popitem()
print(f"After random removing: {d}")
print()
print("UPDATE:")
first=dict(a=1,b=2,c=3,d=4,e=5)
second={}
third=dict(f=6)
print(f"first: {first}")
print(f"second: {second}")
print(f"third: {third}")
second.update(first)
print(f"Second after update with item from first: {second}")
second.update(third)
print(f"Second after update with item from third: {second}")

print("------------------------")
print()
##################################################################################
# This code picks a random food item:
from random import choice
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]  )  
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
    print(f"We don't make {food}")

##################################################################################

