# the syntax
# [__ for __ in __]
# [output_expression for element in list]

num = [1,2,3]
print([ x*10 for x in num ])


names=["andreja","radica","kaja"]
#only first letter uppercase
names_uppercase = [name[0].upper() + name[1:] for name in names]
print(names_uppercase)
# all letter uppercase
all_uppercase=[name.upper() for name in names]
print(all_uppercase)

char_name = 'Andreja'
print([ char.upper() for char in char_name])

print([bool(val) for val in [0, ["andreja"],'']])

numbers=[1,2,3,4,5]
print(f"List of numbers: {numbers}")

# convert to list of string
string_list=[str(num) for num in numbers]
print(f"String list of numbers: {string_list}")

#List comprehension with conditional logic
num_list=[1,2,3,4,5,6,7,8,9,10]
evens= [ num for num in num_list if num % 2 == 0 ]
odds= [ num for num in num_list if num % 2 != 0 ]
print(f"Even number: {evens}")
print(f"Odd number: {odds}")

# print only even number and replace odd with * and using else
changed_list=[ num*2 if num % 2 == 0 else '*' for num in num_list]
print(changed_list)

answer = [char[0] for char in ["Elie","Tim","Matt"]]
print(answer)
answer2 =[num for num in [1,2,3,4,5,6] if num %2 ==0 ]
print(answer2)

# same with loops
# answer = []
# for person in ["Elie", "Tim", "Matt"]:
#     answer.append(person[0])

# answer2 = []
# for num in [1,2,3,4,5,6]:
#     if num % 2 == 0:
#         answer2.append(num)

# intersection of two list
list1=[1,2,3,4]
list2=[3,4,5,6]
answer = [num for num in list1 if num in list2]
print(answer)

# each word reversed and in lowercase
names=["Elie","Tim","Matt"]
answer=[name[::-1].lower() for name in names]
print(answer)

# List of numbers from 1 to 100 that are divisible by 12
number=(range(1,101))
answer = [ num for num in number if num % 12 ==0]
print(answer)

start_string='amazing'
answer=[ char for char in start_string if char not in ["a","e","i","o","u"] ]
print(answer)



