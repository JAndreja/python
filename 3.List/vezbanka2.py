first_list = [ "a", "b", 1 , 3 , True]
print(first_list)
print(len(first_list))

range_list = list(range(1,20))
print(range_list)
print(len(range_list))

names = [ "Andreja", "Radica", "Kaja"]
print(names[0])
print(names[1])
print(names[2])
print(names[-3])
print(names[-2])
print(names[-1])
print("Andreja" in names)
print("andreja" in names)

if "Andreja" in names:
    print ("Hello Andreja")
else:
    print( "Sorry , you are not Andreja")

if "Aleksandar" in names:
    print ("Hello Andreja")
else:
    print( "Sorry , you are not Andreja")

nums = [ 1,2,3,4,5,6]

for num in nums:
    print(num)

number = range(10,20)
i = 0

while i < len(number):
    print(number[i])
    i += 1

letter = [ "a", "b", "c", "d", "e", "f"]

for l in letter:
    print(l.upper())

combine_letter = ''

for i in letter:
    combine_letter +=(f"{i.upper()}-")
print(combine_letter)

nums = [3,40,1,24,5,7,60,25,34,2,8,22,26,57]
list1= []
list2= []

for num in nums:
    if num < 10:
        list1.append(num)
        list1.sort()
    else:
        list2.append(num)
        list2.sort()
print(list1)
print(list2)