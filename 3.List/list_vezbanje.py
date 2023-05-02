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