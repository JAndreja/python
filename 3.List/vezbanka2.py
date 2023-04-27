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


names = ["Andreja", "Radica", "Kaja", "Maza"]

friends = (", ".join(names))

print(f"I'm friend with: {friends}")


list_num = [ 2 ,4 , 6, 8]

duble_num = [ x*2 for x in list_num]
duble_num2 = [ str(x*2) for x in list_num]

print(duble_num)
print(type(duble_num))
print(duble_num2)
print(type(duble_num2))


numbers = [ 1,2,3,4,5,6]

double = [num*2 for num in numbers]
print(double)

double_even = [ num*2 for num in numbers if num % 2 ==0]
print(double_even)

change_odd = [ num*2 if num%2 == 0  else 'odd' for num in numbers]

print(change_odd)


l1= [1,2,3,4]
l2= [3,4,5,6]

answer = [ num for num in l1 if num in l2 ]
print(answer)

names = [ "Elie" , "Tim" , "Matt"]

answer2 = [ name[::-1].lower() for name in names]
print(answer2)

answer3 = [ num for num in range(1,101) if num % 12 == 0]
print(answer3)

start_string = "amazing"
answer4 = [  l for l in start_string if l not in ("a","e","i","o","u") ]
print(answer4)


answer5 = [ name[0] for name in names ]
print(answer5)

l3 = [ 1,2,3,4,5,6]

answer6 = [ num for num in l3 if num %2 == 0]
print(answer6)


nested_list = [ [1,2,3], [4,5,6], [7,8,9] ]

for x in nested_list:
    print(x)
    for y in x:
        print(y)

i = 0

while i < len(nested_list):
    print(nested_list[i])
    i+=1

i=0

i=0
while i < len(nested_list):
     print(f"Index {i}: {nested_list[i]}")
     sub_list=nested_list[i]
     j=0
     while j < len(sub_list):
         print(f"Sub_index {j}: {sub_list[j]}")
         j += 1
     i +=1

nested_list2 = [ [100, 200, 300] , [ 400, 500, 600 ] , [700, 800 , 900 ]]
[[print(val) for val in i] for i in nested_list2]

nested_num=[[1,3,5],[2,4,6],[7,9,11],[8,10,12]]
[[print(val) for val in i] for i in nested_num]

print([["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)])


answer8 = [[num for num in range(0,3)] for x in range(0,3)]
print(answer8)