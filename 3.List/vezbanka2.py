name_list = [ "Andreja", "Radica", "Kaja", "Maza"]

dolzina = len(name_list)
print(dolzina)

print(name_list)
print(name_list[0])

for name in name_list:
    print(name)

i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1

name_list.append("Moli")
print(name_list)

name_list.extend(["Buba","Ljubisha","Dushica"])
print(name_list)

print(name_list.index("Andreja"))
print(name_list.count("Andreja"))
name_list.reverse()
print(name_list)

letters = [ "A", "N", "D", "R", "E", "J", "A"]

print("".join(letters))

num = [ 1 ,2, 3 ,4 , 5 ,6]
print(type(num))
num_str=str(num)
print(type(num_str))
print(type("".join(str(num))))
print(type("".join(num_str)))

num_str1 = [ "1","2","3","4"]
print(type("".join(num_str1)))