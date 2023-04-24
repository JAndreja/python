#syntax
# { ____:____ for ___ in ____}

numbers=dict(first=1,second=2,third=3)
squared_number={key:value**2 for key,value in numbers.items()}
print(squared_number)

numbers={num:num*2 for num in [1,2,3,4,5]}
print(numbers)

str1= "ABC"
str2 = "123"
combo={str1[i]:str2[i] for i in range(0,len(str1))}
print(combo)

for key,value in combo.items():
    print(f"{key}:{value}")
    
person = { "name":"andreja", 'surname':"jovanovski"}
upper_person={ key:value.upper() for key,value in person.items()}
print(upper_person)
    
#conditional logic with dictionaries
num_list =[1,2,3,4]
num_dic={ num:("even" if num %2 ==0 else "odd") for num in num_list}
print(num_dic)

print("================================================================")


#################################################################################
# exercise
print()
print("exercise 1:")
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer = {list1[i]:list2[i] for i in range(0,len(list1))}
print(answer)

print()
print("exercise 2:")
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
solution1= {p[0]:p[1] for p in person }
print(solution1)
solution2 = {k:v for k,v in person}
print(solution2)
solution3 = dict(person)
print(solution3)

print()
print("exercise 3:")
answer={char:0 for char in 'aeiou'}
print(answer)

print()
print("exercise 4:")
answer={count:chr(count) for count in range(65,91)}
print(answer)