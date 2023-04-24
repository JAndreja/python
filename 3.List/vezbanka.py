demo_list = [ 1, "a", 0.5 , True]

print(demo_list)
print(f"Listata ima: {len(demo_list)}")

nums=list(range(2,101,2))
print(nums)

print(nums[-1])

for element in demo_list:
    print(element)
    
num_list =list(range(0,21))
x=0
while x < len(num_list):
   if num_list[x] %2 == 0:
       print(f"{num_list[x]} is even ")
       x +=1
   else:
       print(f"{num_list[x]} is odd") 
       x += 1
       
name_list=["Andreja","Radica","Kaja"]
print(name_list)
print(len(name_list))
name_list.append("Maza")
name_list1=name_list
print(name_list1)
print(len(name_list1))
name_list.append(["Maza","Paza"])
name_list2=name_list
print(name_list2)
print(len(name_list2))

name_list3=["Andreja","Radica","Kaja"]
name_list3.extend(['Maza'])
print(name_list3)
print(len(name_list3))
name_list3.extend(['Maza','Paza'])
print(name_list3)
print(len(name_list3))

names=['andreja','radica','kaja']

for name in names:
    print(name)
    #print(name[0].upper()+name[1:])
    
print([name[0].upper() + name[1:] for name in names])

print([bool(val) for val in [0, ["andreja"],'']])

numbers=[1,2,3,4,5]
print(f"List of numbers: {numbers}")

# convert to list of string
string_list=[str(num) for num in numbers]
print(f"String list of numbers: {string_list}")


num_list =list(range(0,11))
print(num_list)

change_list=[ f" {num} is even" if num%2 == 0 else f" {num} is odd" for num in num_list]
print(change_list)

change_list2=[ num for num in num_list if num%2 ==0 ]
print(change_list2)

num_list=[1,2,3,4,5,6,7,8,9,10]
evens= [ num for num in num_list if num % 2 == 0 ]
odds= [ num for num in num_list if num % 2 != 0 ]
print(f"Even number: {evens}")
print(f"Odd number: {odds}")

list1=[1,2,3,4]
list2=[3,4,5,6]
for num in list1:
    if num in list2:
        print(num)
answer=[ num for num in list1 if num in list2]
print(answer)


nested_list = [[1,2,3],[4,5,6],[7,8,9]]

for i in nested_list:
    print(i)
    #for j in i:
     #   print(j)

i=0

while i < len(nested_list):
    #print(f"Index {i}:")
    sub_list=nested_list[i]
    j=0
    while j < len(sub_list):
        print(f"Indexing [{i}][{j}]: {sub_list[j]}")
        j += 1
    i += 1
print("--------------------------------------")  


num_range = list(range(0,101))

answer=([num for num in num_range if num % 12 ==0 ])
print(f"Even number: {answer}")

