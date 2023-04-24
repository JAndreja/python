
# string_list = [ "Andreja", "Radica"]

# for names in string_list:
#       print(f"String name {names} is {len(names)} character long")
#       i= 0
#       while i < len(names):
#           print(f"{i+1} character is: {names[i]}")
#           i += 1 
          

# num_list= [4,2,5,1,10,7,8,22,33]
# even_list =[]
# for num in num_list:
#     if num % 2 == 0:
#         even_list.append(num)
#         even_list.sort()
# print(even_list)

# new_list=([num for num in num_list if num % 2 ==0])
# new_list.sort()
# print(new_list)
# num_test_list = [20,30,40]
# add_list=[50,60]

# num_test_list.append(add_list)
# print(num_test_list)
# num_test_list.extend(add_list)
# print(num_test_list)
# num_test_list.insert(0,add_list)
# print(num_test_list)

# nums=[10,14,23,11,22]
# i = 0
# while i < len(nums):
#     print(f'{i}:',nums[i])
#     i += 1 
    
# brojki =[1,2,3,4,5,6,7,8]

# print([n*2 for n in brojki if n%2 ==0])
# print([n*2 if n%2 ==0 else f"{n}" for n in brojki])


# answer = [char[0] for char in ["Elie","Tim","Matt"]]
# print(answer)

# nested_list = [ [1,2,3], [4,5,6], [7,8,9] ]

# for i in nested_list:
#     print(i)
#     # for j in i:
#     #     print(j)

# i=0
# while i < len(nested_list):
#     print(f"Index {i}: {nested_list[i]}")
#     i  +=1
    
# i = 0 
# while i < len(nested_list):
#     print(f"Index {i}: {nested_list[i]}")
#     sub_list=nested_list[i]
#     k = 0
#     while k < len(sub_list):
#         print(f"SubIndex {k}: {sub_list[k]}")
#         k += 1
#     i += 1
 
    
# nested_num=[[1,3,5],[2,4,6],[7,9,11],[8,10,12]]

# print([i for i in nested_num])
# [[print(val) for val in i] for i in nested_num]

# print('****************************************')

# char_list= ["A","n","D","r","E","j","A"]

# string_name=[c for c in char_list]
# # join_string="".join(string_name)
# # print(join_string)

# lists = []
# for i in range(4):
#     lists.append([])
#     for j in range(5):
#         lists[i].append(j)
# print(lists)

# lists = []
# for i in range(2): 
#     lists.append([]) 
#     for j in range(5): 
#         lists[i].append(j) 
# print(lists)

    
# list1 = [ "name", "surname", "age"]
# list2 = ["Andreja", "Jovanovski", "44"]

# new_dict ={}
# for key in list1:
#     for value in list2:
#         new_dict[key] = value
#         list2.remove(value)
#         break
# print(new_dict)



# d = dict (a="Andreja", b=1 , c= False)

# print(d.get('a'))
# print(d.get('Andreja'))

# str1= "ABC"
# str2 = "123"
# combo={str1[i]:str2[i] for i in range(0,len(str1))}
# print(combo)

# def return_day(num):
#     days = ["Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
#     if num > 0 and  num <=len(days):
#         return days[num-1]
#     return None
# print(return_day(1))
          
# def return_day1(num):
#     days = { 1:"Monday", 2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday" }
#     day = days.get(num)
#     if day:
#         return day
# print(return_day1(2))
# print(return_day1(8))

# def last_element(list):
#     if list:
#         return list.pop()
#     return None
    
# print(last_element([1,2,3,4,1,2]))
# print(last_element([]))


# def num_copmare(num1, num2):
#     if num1 > num2:
#         return "First is greather"
#     elif num1 < num2:
#         return "Second is greather"
#     return "Numbers are equal"
    
    
# print(num_copmare(10,4))
# print(num_copmare(4,10))
# print(num_copmare(4,4))

# def single_letter_count( string, letter):
#     return string.count(letter)
            
# print(single_letter_count('andreja','a'))
# print(single_letter_count("banana","a"))


# def multi_letter_count(string):
#     return {i:string.count(i) for i in string}

# print(multi_letter_count("andreja"))
# print(multi_letter_count("awesome"))
# print(multi_letter_count("Aaaaaaaaaaaa"))


# def list_manipulation(collection,command,location,value=None ):
#     if command == "remove" and location == "end":
#         return collection.pop()
#     elif command == "remove" and location == "beginning":
#         return collection.pop(0)
#     elif command == "add" and location == "beginning":
#           collection.insert(0,value)
#           return collection
#     elif command == "add" and location == "end":
#          collection.append(value)
#          return collection
    
# print(list_manipulation([1,2,3], "remove", "end"))
# print(list_manipulation([1,2,3], "remove", "beginning"))
# print(list_manipulation([1,2,3], "add", "beginning", 20))
# print(list_manipulation([1,2,3], "add", "end", 30))

# def is_palindrom(string):
#     if string == string[::-1]:
#         return True
#     return False
# print(is_palindrom("testing"))
# print(is_palindrom("tacocat"))

# def frequency(list,term):
#     return list.count(term)

# print(frequency([1,2,3,4,4,4],4))
# print(frequency([True, False, True, True], False))


# def multi_even_numbers(nums):
#     total = 1
#     for num in nums:
#         if num % 2 == 0:
#             total = total*num
#     return total
              
# print(multi_even_numbers([2,3,4,5,6]))     



# def test(**kwname):
#     return kwname['Radica']

# print(test(Andreja='1' , Radica='2'))


# def test(*args):
#     print(args)
    
# nums=[1,2,3,4,5,6]
# nums2=(1,2,3,4,5)
# test(nums)
# test(*nums)
# test(nums2)
# test(*nums2)

# nums = [2,4,6,8]


# def double(num):
#     print(num)
#     return num*2

# double_map = map( double, nums)
# print(list(double_map)) 

# double_map1 = map( lambda num: num*2, nums)
# print(list(double_map1))


# def remove_negatives(nums):
#     #return [num for num in nums if num > 0]
#     return [num if num > 0 else '*' for num in nums]

# print(remove_negatives([-1,3,4,-99]))

# lists = []
# for i in range(3):
#     lists.append([i])
#     for j in range(3):
#         lists[i].append(j)
# print(lists)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# list1=[2,3,5,6]
# list2=[7,1,4,8]

# new_list =[]
# for i in range(len(list1)):
#     new_list.append([list1[i]])
#     for k in list2:
#        new_list[i].append(k)
#        list2.remove(k)
#        break
# print(new_list)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# name = "Andreja"

# for n in name:
#     print(n)
        
# name_comp=[i for i in name]
# print(name_comp)

# new_name = []
# for n in "Radica":
#     print(n)
    
# for n in "Radica":
#     new_name.append(n)
# print(new_name)

# name_comp2=[ letter for letter in "Radica"]
# print(name_comp2)

# numbers=[3,6,7,1,2]

# for i in numbers:
#     print(f"Index[{numbers.index(i)}]:{i}")
    
# for i in range(len(numbers)):
#     print(numbers[i])
    


# user = { "name": "Andreja",
#            "surname": "Jovanovski",
#             "age": 46,
#             "own_dog": False}

# print(user['name'])
# print(user)
# print(f"{user['name']} {user['surname']}")

# for key in user.keys():
#     print(key)
    
# for val in user.values():
#     print(val)
    
# for k,v in user.items():
#     print(f"{k}:{v}")

# dict1 = {}.fromkeys( "a" , "b")
# print(dict1)

# seq = ( 'a', 'b', 'c','d')

# dict2 = dict.fromkeys(seq)
# print(dict2)

# dict3 = dict.fromkeys(seq,2)
# print(dict3)

# dict4 = dict.fromkeys(['Name','Surname'], 'NONE')
# print(dict4)


# person = dict( name='Andreja' , age =45 )

# print( 'Name:', person.get('name'))

# letter = ( 'a', 'b', 'c', 'd')
# num = ( 1,2,3,4)

# letter_number = {letter[l]:num[l] for l in range(0, len(letter))}
# print(letter_number)

# num_list = [1,4,2,6,9,10]

# num_dict = { n:("even" if n %2 ==0 else "odd") for n in num_list}
# print(num_dict)

# s = ({2,1,3,6,1,1,7,4,4,5,5})

# print(s)

# def sum():
#     print(7+7)

# sum()

# def sum1():
#     return 7+7

# print(sum1())

# def hello(name):
#     return f"Hello {name}"

# print(hello('Andreja'))

# def hello1(name,surname):
#     return f"Hello {name} {surname}"

# print(hello1('Andreja','Jovanovski'))

# def hello2(name,surname="Jovanovski"):
#     return f"{name} {surname}"


# print(hello2('Andreja','Petrovski'))


# name = "Radica"

# def say_hi():
#     return f"Hello {name}"



# print(say_hi())
# print(name)


# def nums(*num):
#     print(num)
    
# nums(1,2,34,4)

# def check_nums(*num):
#     if 4 in num and 5 in num :
#         return 'OK'
#     return 'NO'

# print(check_nums(1,2,3,4,5,6))
# print(check_nums(1,2,3,6,7))


# def sum_all(*nums):
#     print(nums)
#     total = 0
#     for num in nums
#         total += num
#     print(total)
    
# #sum_all(1,2,3,4)

# #sum_all((1,2,3,4))
# #sum_all(*(1,2,3,4))

# #sum_all([1,2,3,4])
# sum_all(*[1,2,3,4])


# def display_names(**full_names):
#     print(full_names)
#     for name , last_name in full_names.items():
#         print(f"{name} {last_name}")
    
# #display_names(Andreja="Jovanovski", Radica= "Jovanovski", Kaja="Jovanovski")
# #display_names(**{ "Andreja":"Jovanovski","Radica":"Jovanovski","kaja":"Jovanovski"})


# def add_num_multiply_num(a,b,c):
#     print(a+b*c)

# data = dict(a=1,b=2,c=3)
# #add_num_multiply_num(data)
# add_num_multiply_num(**data)




# sum = lambda x,y: x+y

# print(sum(1,2))

# def sum(x,y):
#     return x+y

# print(sum(3,4))

# nums = [ 1,2,3,4]

# def sum(x):
#     return x+x

# sum_map = map(sum,nums)
# #print(list(sum_map))
# #print(tuple(sum_map))
# #print(set(sum_map))

# sum_lambda = list(map(lambda x: x+x, nums))
# print(sum_lambda)

# names = [{"name":"Andreja", "surname":"Jovanovski"},
#          {"name":"Radica", "surname":"Mihajlovski"}]

# map_names = map( lambda n: n['name'] , names)
# print(list(map_names))


# for name in names:
#     print(name["surname"])
    
# new_list= [ name['surname'] for name in names]
# print(new_list)

# new_list=[]
# def dec(num_list):
#     for i in num_list:
#         new_list.append(i-1)
#     print(new_list)

# dec([50,60,70])
        
# numbers = [50,60,70]

# new_list1=map(lambda i: i-2, numbers)
# new_list1=list(new_list1)
# print(new_list1)

# list_comp=[ i-3 for i in numbers]
# print(list_comp)

# nums = [1,2,3,4]

# even_map = map ( lambda num: num%2 ==0,nums)
# print(list(even_map))
# even_filter = filter( lambda num: num%2 ==0,nums)
# print(list(even_filter))

# num_list = [-1,3,4,-99]

# new_list =[]
# for num in num_list:
#     if num > 0:
#         new_list.append(num)
# print(new_list)

# filter_num = filter( lambda num : num > 0, num_list)
# print(list(filter_num))


# list_com=[ num for num in num_list if num > 0]
# print(list_com)

# list_map= map(lambda num : num > 0 , num_list)
# print(list(list_map))


# names= [ 'Arya', 'Samson', 'Dora','Tim', 'Ollivander' ]

# name= [len(name) for name in names]
# print(name)
# name1=min(len(name) for name in names)
# print(name1)

# nums = [1,2,3,4]

# print(sum(nums,5))

# num_list1 = [ 1,2,3,4]
# num_list2 = [ 5,6,7,8]

# combine_list = zip(num_list1,num_list2)
# #print(list(combine_list))
# print(dict(combine_list))


# midterm = [80,91,78]
# finals = [98,89,53]
# students = [ 'dan', 'ang', 'kate']

########################################
# comb_score = zip(midterm,finals)
# max_score =[]
# for pair in comb_score:
#     max_score.append(max(pair))
# print(max_score)
# finals = zip(students,max_score)
# print(dict(finals))
######################################################
# zip_list = zip(students,midterm,finals)
# print(list(zip_list))
###########################################################
# final_grades={pair[0]:max(pair[1],pair[2])for pair in zip(students,midterm,finals)}
# print(final_grades)
#############################################################
# map_list =zip(students, map(lambda pair:max(pair), zip(midterm,finals)))
# print(dict(map_list))



# def inter( str1, str2):
#     join_str=[]
#     for x in zip(str1,str2):
#         join_str.append(''.join(x))
#     return ''.join((join_str))
    
# print(inter('Adea ','nrj '))
                   
# def inter2(str1,str2):
#     return ''.join(''.join(x) for x in (zip(str1,str2)))

# print(inter2('Adea ','nrj '))



# def triple_and_filter(nums):
#     new_list =[]
#     for num in nums:
#         if num %4 ==0:
#             new_list.append(num*3)
#     return new_list
    
# def triple_and_filter2(nums):
#     return [num*3 for num in nums if num%4 ==0]

# def triple_and_filter3(num_list):
#     return list(filter(lambda num: num%4 ==0, map(lambda num:num*3,num_list)))



# print(triple_and_filter([1,2,3,4]))
# print(triple_and_filter([6,8,10,12]))

# print(triple_and_filter2([1,2,3,4]))
# print(triple_and_filter2([6,8,10,12]))

# print(triple_and_filter3([1,2,3,4]))
# print(triple_and_filter3([6,8,10,12]))


# multi_list = [('Andreja','Radica'),('Kaja','Buba')]
# #print(type(multi_list))
# #print(multi_list)

# for i in multi_list:
#     print(i)
#     for k in i:
#         print(k)
        

