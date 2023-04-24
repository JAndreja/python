names_dict = { "name": "Andreja",
                "surname": "Jovanovski",
                "age": "45",
                "own_cat": False
                }

print(names_dict)
print(type(names_dict))
print("-----------------")
print(names_dict.keys())
print(type(names_dict.keys()))
print("-----------------")
print(names_dict.values())
print(type(names_dict.values()))
print("-----------------")
print(names_dict.items())
print(type(names_dict.items()))

d1 =dict( a=1 , b=2, c=3)
d2 = d1.copy()
print(d2)
print(d1 is d2)
print(d1 is not d2)

for key in names_dict.keys():
    print(key)
    
for value in names_dict.values():
    print(value)
    
for k,v in names_dict.items():
    print(f"{k}:{v}")
print( "Andreja" in names_dict.values())
print( "Radica" in names_dict.values())

print( "name" in names_dict.keys())
print( "color" in names_dict.keys())

print( "name" in names_dict)
print("******************************************************************")
print("******************************************************************")
print()

dict3={}.fromkeys( "a", "1")
print(dict3)

dict4 = {}.fromkeys( [ "a" ,"b"], ["1","2"])
print(dict4)

get_dict=dict(a=1 , name='Andreja', favorite_number= 45,dog_owner = True)
print(get_dict.get('name'))

for k in get_dict.keys():
    print(get_dict.get(k))
    
list1 =["a","b","c"]
list2 = [1,2,3]

# res ={}
# for key in list1:           
#     for value in list2:
#       res[key] = value
#       list2.remove(value)
#       break
# print(res)

res1 = {list1[i]:list2[i] for i in range(0,len(list2))}
print(res1)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
solution = { p[0]:p[1] for p in person}
print(solution)