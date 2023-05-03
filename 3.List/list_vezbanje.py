numbers = [ 1,2,3,4,5,]
print(numbers)
print(len(numbers))

colors = ["red", "green","blue"]
print(colors)
print(len(colors))

coordinates = [ [0,0], [100,200] , [300,400]]
print(coordinates)
print(len(coordinates))

print(numbers[0])
print(numbers[-2])
print(colors[1])
print(coordinates[2])

for num in numbers:
    print(num)

for num in enumerate(numbers):
    print(num)

for index , num in enumerate(numbers):
    print(f"index {index}: {num}")


i = 0
while i < len(numbers):
    print(f"index {i}: {numbers[i]}")
    i += 1

y =0
while y < len(coordinates):
    print(f"index {y}: {coordinates[y]}")
    y += 1

list1 = [1,2,3,4]
list2 = [5,6,7,8]

list1.append(list2)
print(list1)
list1.extend(list2)
print(list1)
list1.extend([9,10,11,12])
print(list1)
list1.insert(0,0) 
print(list1)
list2.clear()
print(list2)

prime_numbers = [2, 3, 5, 7]

removed_element = prime_numbers.pop(2)
print(f"Removed element: {removed_element}")
print(f"Updated List: {prime_numbers}")


num3 = [1,2,3,4,5]
num4 = [6,7,8,9]
print(num3)
print(type(num3))
print("".join(str(num3)))
print(type("".join(str(num3))))

print("/".join(str(num3)))


name1 = "andreja"

name_upper = f"{name1[0].upper()}{name1[1:]}"
print(name_upper)