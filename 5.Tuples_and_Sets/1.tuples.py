# tuple syntax
# number= (     )
#tuple can never be changed!!!!!

first_tuple = (1, 2, 3, 3, 3)
#Accessing value in tuple
print(first_tuple[1])
print(first_tuple[-1])


#looping
names = ('Andreja','Radica','Kaja')
for name in names:
    print(name)
print("-------------------------------")
i=0
while i < len(names):
    print(names[i])
    i += 1
print("-------------------------------")

i = len(names)-1
while i >= 0:
    print(names[i])
    i -= 1
print("-------------------------------")
# Tuple methods (count, index)
#count method
print(first_tuple.count(1))
print(first_tuple.count(3))

#index method
print(names.index("Andreja"))
print(names.index("Kaja"))

