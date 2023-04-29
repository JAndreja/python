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