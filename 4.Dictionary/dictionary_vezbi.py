country_capital = { 
                    "Nepal":"Kathmandu",
                    "Italy": "Rome",
                     "England": "London" }

print(country_capital)
print(country_capital["Nepal"])
print({f"Capital of Nepal is {country_capital['Nepal']}"})

numbers = {1: "One", 2: "Two", 3: "Three"}
print(numbers)

for key in country_capital.keys():
    print(key)

for value in country_capital.values():
    print(value)

for k ,v in country_capital.items():
    print(f"Capital of {k} is {v}")


print('Nepal'in country_capital.keys())
print('Macedonia'in country_capital.keys())

print('Skopje' in country_capital.values())
print('Rome' in country_capital.values())


delete_dict = {"a":"1", "b":"2" , "c":"3"}

delete_dict.clear()
print(delete_dict)

copy_dict = {"a":"1", "b":"2" , "c":"3"}
clone = copy_dict.copy()
print(clone)

print(f"a:{clone.get('a')}")
print(f"d: {clone.get('d')}")