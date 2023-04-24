
# test_list=["Andreja","Radica","Kaja"]
# i =0
# while i < len(test_list):
#     print(test_list[i])
#     i += 1
print("==========================================")

print("** WITH FOR LOOPS **")
num_list=[1,2,3,4,5,6,7,8,9,10]
num_even=[]
num_odd=[]
for num in num_list:
    if num %2 ==0:
        num_even.append(num)
    else:
        num_odd.append(num)       
print(f"Even number: {num_even}")
print(f"Odd number: {num_odd}")

print("==========================================")

print("** WITH LIST_COMPREHENSION **")

evens= [ num_even for num_even in num_list if num_even % 2 == 0 ]
odds= [ num_odd for num_odd in num_list if num_odd % 2 != 0 ]
print(f"Even number: {evens}")
print(f"Odd number: {odds}")

print("==========================================")

print("** WITH FOR LOOPS **")
char_list= ["A","n","D","r","E","j","A"]
string=[]
#for c in char_list:
#    string.append(c)
test_string="".join(char_list)
print(test_string.upper())

print("==========================================")

print("** WITH LIST_COMPREHENSION **")

string=[ c for c in char_list]
join_string="".join(string)
print(join_string.upper())