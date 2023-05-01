demo_list =["a","b",1.5,3, True]
print(demo_list)

# broj na elementi vo lista
#len(demo_list))
print("===============")
print("** Broj na elementi vo lista **")
dolzina=len(demo_list)
print(f"Listata ima {dolzina} elementi")

# create list with function list
print("===============")
print("** Create list with function list **")
number=list(range(1,5))
print(number)

# accessing values in a list
print("===============")
print("** Accessing values in a list **")
names=["andreja","radica","kaja"]
print(names)
print(names[0])
print(names[1])
print(names[2])

# accessing values from the end
print("===============")
print("** Accessing values from the end **")
print(names)
print("From the end: " + names[-1])
print("From the end: " + names[-3])

#accessing value in a list with for loops
print("===============")
print("** Accessing value in a list with for loops **")
print(names)
for name in names:
    print(name)

#accessing value in a list with while loops
print("===============")
print("** Accessing value in a list with while loops **")
num=[1,2,3,4,5]
print(num)
#num = list(range(1,11))
i=0
while i < len(num):
    print(f"Index {i}: {num[i]}")
    i += 1
    
#list methods ( append,extend,insert )
print("===============")
print("** List Methods ( append, extend, insert ) **")
num_list=[1,3,5,7,9]
print(f"List: {num_list}")
#APPEND#
# can only append one argument (add a new element to the end of a list)
num_list.append(20)
#  output  [ 1,3,5,7,9, [30,40,50]] adedd as a one argument    
num_list.append([30,40,50])   
print(f"List after appending a number: {num_list}")
#EXTEND#
# can added as many you want argument
num_list.extend([21,34,56,78])    
print(f"List after extending with numbers : {num_list}")
#INSERT#
# insert an item at a given position  (add a new element at a position in a list.)
num_list.insert(2,"Hello")
print(f"List after insert values: {num_list}")

#list methods ( clear, pop,remove)
print("===============")
print("* List Methods ( clear , pop , remove ) **")
print("---------------------------")
name_list=["andreja","radica","kaja"]
print(f"List before clearing: {name_list}")
#CLEAR#
name_list.clear()
print(f"List after clearing: {name_list}")
print("---------------------------")
name_list=["andreja","radica","kaja"]
print(f"List before pop: {name_list}")
#POP#  to remove an element from a list and return that element.
print("Removed: " + name_list.pop())  
print(f"List after pop with not specified index position(remove last element) : {name_list}")
print("---------------------------")
name_list=["andreja","radica","kaja"]
print(f"List before pop: {name_list}")
print("Removed: " + name_list.pop(1))
print(f"List after pop with specified index position : {name_list}")
print("---------------------------")
name_list=["andreja","radica","kaja","andreja","radica","kaja"]
print(f"List before remove: {name_list}")
#REMOVE# to remove an element from a list.
name_list.remove("andreja")
print(f"List after remove the first item in list with value 'Andreja' : {name_list}")

#list methods ( index, count, sort , reverse , join )
print("===============")
print("** List Methods ( index, count, sort , reverse , join ) **")
num=[10,14,23,11,22]
print(f"List: {num}")
print(f"Number 22 index is : {num.index(22)}")
print(f"Number 14 index is : {num.index(14)}")
print("---------------------------")
num=[1,2,3,5,2,4,6,3,1,1,3,5,2,3,3,3,5,5,5,2,2,2]
print(f"List: {num}")
print(f"Number 3 apears: {num.count(3)} times")
print(f"Number 5 apears: {num.count(5)} times")
print(f"Number 2 apears: {num.count(2)} times")
print("---------------------------")
reverse_list=[1,2,3,4,5]
print(f"List before revers: {reverse_list}")
reverse_list.reverse()
print(f"Revers order of numbers: {reverse_list}")
print("---------------------------")
sort_list=[1,4,2,7,3,5]
print(f"List before sorted: {sort_list}")
sort_list.sort()
print(f"Sorted list: {sort_list}")
print("---------------------------")
words = [ "Andreja", "Jovanovski", "testira", "Python"]
num = [1,2,3,4,5]
num1 = ["1","2","3","4","5"]
num=str(num)
print(words)
print(num)
string=" ".join(words)
print(string)
print("/".join(words))
print("".join(num))
print("".join(num1))

# Slicing
print("===============")
print("Slicing")
# some_list[start:end:step]
list_num=["red", "blue", "green","violet","orange", "yellow"]
print(list_num)
print(f"Specified index where to start slicing (INDEX 1): {list_num[1:]}")
print(f"Specified index where to start slicing (INDEX 3): {list_num[3:]}")
print(f"Specified index where to start slicing (INDEX 0) and where to end (INDEX 4): {list_num[:4]}")
print(f"Specified index where to start slicing (INDEX 2) and where to end (INDEX 5): {list_num[2:5]}")
print(f"Specified index where to start slicing (INDEX 2) and where to end (INDEX 6): {list_num[2:6]}")
print(f"Specified index where to start slicing (INDEX 0) and where to end (INDEX 6) and step: {list_num[0:6:2]}")
print(f"Reverse order of list: {list_num[::-1]}")
print(f"Select element from list and revers order of string: {list_num[3][::-1]}")
print(list_num[-2])