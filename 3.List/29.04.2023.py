names = [ "Andreja" , "Radica" , "Kaja"]
print(names)

for name in names:
    print(f"Hello {name}")

print([ name for name in names])
print([ name.upper() for name in names])

print([name[0].lower() + name[1:] for name in names])

new_list =[]
for name in names:
    new_list.append(name[0].lower()+ name[1:])
print(new_list)


name = "andreja"

print(name[0])

for s in name:
    print(s)

i = 0

while i < len(name):
    print(f"letter {i+1}: {name[i]}")
    i += 1


nested_list = [ [1,2,3], [4,5,6], [7,8,9] ]


for i in nested_list:
    for y in i:
        print(y)

i =0 
while i < len(nested_list):
    print(nested_list[i])
    sub_list = nested_list[i] 
    y=0
    while y < len(sub_list):
        print(sub_list[y])   
        y += 1
    i += 1

