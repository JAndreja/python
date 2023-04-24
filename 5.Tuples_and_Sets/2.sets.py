# Sets cannot have duplicates
s = set({1, 2, 3, 4, 5, 5, 5}) # {1, 2, 3, 4, 5}

# Creating a new set
s = set({1, 4, 5})

# Creates a set with the same values as above
s = {1, 4, 5}

4 in s
# True

8 in s
# False

#looping
numbers = {1,2,3,4}
for number in numbers:
    print(number)
print("-------------------------") 
# Set Methods (add,remove,copy,clear)
#add
num = { 1,3,5,7,2}
print(f"Before adding a number: {num}")
num.add(11)
print(f"After adding a number: {num}")
#remove
num1 = { 1,2,3,4,5,6}
print(f"Before removing: {num1}")
num1.remove(3)
print(f"After removing number 3 : {num1}")
#copy
names2 = { "test", "test1","test2"}
print(names2)
names3 = names2.copy()
print(names3)
#clear
color= { "red", "blue", "green"}
print(f"Before clearing: {color}")
color.clear()
print(f"After clearing: {color}")
print("-------------------------") 

# SET MATH
math_student = {"Andreja", "Petko", "Radica", "Stanko", "Kaja", "Buba"}
history_student = {"Janko", "Andreja", "Vesna", "Zarko", "Radica"}

# union
print(f"No duplicate stundent: {math_student | history_student}")

#intersection
print(f"Students how attend both classes: {math_student & history_student}")


#SET COMPREHENSION

print({x**2 for x in range(10)})

