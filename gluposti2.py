# List = ['G', 'E', 'E', 'K', 'S', 'F','O', 'R', 'G', 'E', 'E', 'K', 'S']

# print(List[0::])  # all elements
# print(List[::-1]) # all elements revers

# print(List[3:8])
# print(List[:-4:-1])
# print(List[:3:8])
# print(List[::-2])

# char_list= [ 'A', 'N','D','R','E','J','A']

# print(char_list[::1])
# print(char_list[::-1])

# print(char_list[::2])

# print(char_list[-3:])

# odd_square =[]
# for n in range(1,11):
#     if n %2 ==1:
#         odd_square.append(n**2)
# print(odd_square)

# odd_square1 = [ n**2 for n in range(1,11) if n%2 ==1]
# print(odd_square1)


# odd_square3 = [n**2 if n%2 ==1 else '*' for n in range(1,11)]
# print(odd_square3)

# odd_even = [ 'even' if n%2 == 0 else 'odd' for n in range(1,11)]
# print(odd_even)

# odd_even1 = { num:('even' if num %2 ==0 else 'odd') for num in range(1,11)}
# print(odd_even1)


# person = { '1':'Andreja', '2':'Radica'}
# print(person)
# person1= dict( a='1', b='2' )
# print(person1)


# person = {
#     # key:  value
#     "name":"Andreja",
#     "surname":"Jovanovski",
#     "age": "44",
#     "own_dog": False,
#      44: "favorite number"
# }

# print(person.keys())
# print(person.values())
# print(person.items())

# for k,v in person.items():
#     print(f"{k}:{v}")
    
# d = dict( a=1,b=2,c=3,d=4)

# dict1=dict.fromkeys(['a','b'], 'NONE')
# print(dict1)

# dict2 ={}.fromkeys(['c','d'], '2')
# print(dict2)

# print(d.get('a'))
# print(f"b:{d.get('b')}")

# numbers=dict(first=1,second=2,third=3)

# for k,v in numbers.items():
#     print(k,v)
    
# dict_comp = { k:v*2 for k,v in numbers.items()}
# print(dict_comp)

# letter = ['a','b','c','d']
# nums= [1,2,3,4]
# new_dict = {}


# for i in range(len(letter)):
#       for k in nums:
#          new_dict.update({letter[i]:k})
#          nums.remove(k)
#          break
# print(f"For loop dict: {new_dict}")


# letter = ['a','b','c','d']
# nums= [1,2,3,4]
# dict_com = { letter[i]:nums[i] for i in range(len(letter))}
# print(f"Dict_comp: {dict_com}")



# letter = ['a','b','c','d']
# nums= [1,2,3,4]

# zip_dict=dict(zip(letter,nums))
# print(f"Zip dict: {zip_dict}")

# num_tuple= ( 1,3,4,5,6,1,2)
# print(num_tuple)

# for n in range(len(num_tuple)):
#       print(f"Index {n} : {num_tuple[n]}")
 
# num_tuple= ( 1,3,4,5,6,1,2) 

# i=0     
# while i < len(num_tuple):
#       print(f"Index {i} : {num_tuple[i]}")
#       i += 1

# set1= { "Ime", "Prezime", "Vozrast"}
# set2 = { "Andreja", "Jovanovski", 44}
# print(set1)

# dict_name = dict(zip(set1,set2))
# print(dict_name)

# def test(**words):
#      return f"Hello {words['Name']} your'r favorite color is {words['color']}"


# print(test(Name="Andreja", color="yellow"))

# nums=[1,2,3,4]

# def sum(*num):
#       print(num)
#       total =0
#       for n in num:
#           total += n
#       print(total)
      
# sum(*nums)

# names = { "first": "Andreja", "second": "Jovanovski"}

# def display_full_name(**all):
#       print(all)
#       for first,second in all.items():
#               return f"{all['first']} {all['second']}"

# #display_full_name(**names)   
# print(display_full_name(**names))

# def letter_count(string):
#       return {string[s]:string.count(string[s]) for s in range(0,len(string))}
#       #return {s:string.count(s) for s in string}
      
# print(letter_count("amwlaqeqweaasdda"))

# def square(x):
#       return x*x

# print(square(2))

# square2=lambda x: x*x
# print(square2(2))


# def sum_num(nums):
#       j=0
#       for n in nums:
#             j=n+j
#       return j
# numbers=[1,2,3,4]

# print(sum_num(numbers))
# sum_num1 = map(sum_num,numbers)
# print(list(sum_num1))


# # sum = lambda x,y: x+y
# # print(sum(3,4))

# nums = [1,2,3,4,5]

# sum_num = map( lambda n: n+n, nums)
# sum_num=list(sum_num)
# print(sum_num)


# names= [ 'Arya', 'Samson', 'Dora','Tim', 'Ollivander' ]

# print(min(names, key=lambda n: len(n)))



# square = {2: 4, -3: 9, -1: 1, -2: 4}

# print(max(square, key=lambda k: square[k]))

# sum = 0
# for k in square:
#      sum =sum +square[k]
# print(sum)

# for k in square:
#     print(k)

# test=max(square, key=lambda k:square[k])
# print(test)

# my_dict =dict( {'1':"Andreja",'2':'Radica'})
# my_dict2=dict(name='Andreja', test ='test')
# my_dict3 = dict([(1,'apple'), (2,'ball')])
# print(my_dict)
# print(my_dict2)
# print(my_dict3)
# print(my_dict3[1])
# print(my_dict2.get('name'))

# for val in my_dict.values():
#     print(val)
    
# keys = {'a', 'e', 'i', 'o', 'u' }

# vowels={}.fromkeys(keys)
# print(vowels)
# vowels2={}.fromkeys(keys,'-vowel')
# print(vowels2)

# keys = {'a', 'e', 'i', 'o', 'u' }
# value = []

# vowels=dict.fromkeys(keys,value)
# print(vowels)
# vowel.extend([1,2,3])
# print(vowels)

# keys = {'a', 'e', 'i', 'o', 'u' }
# value = [1]

# vowels = {key:list(value) for key in keys}
# print(vowels)

# new_dict = {}.fromkeys(vowels,value)
# print(new_dict)

# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]

# new_dict={}
# for i in range(0,len(list1)):
#     for j in list2:
#         new_dict.update({list1[i]:j})
#         list2.remove(j)
#         break
# print(new_dict)

# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]

# new_dict={list1[i]:list2[i] for i in range(0,len(list1))}
# print(new_dict)



# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]

# new_list = zip(list1,list2)
# print(dict(new_list))




# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]



# new_dict={}
# for i in list1:
#     for j in list2:
#         new_dict.update({i:j})
#         list2.remove(j)
#         break


# pow =[]
# for x in range(10):
#     pow.append(x**2)
# print(pow)
    
# pow2 = [x**2 for x in range(10)]
# print(pow2)

# h_letter = []
# for l in 'human':
#     h_letter.append(l)
# print(h_letter)

# h_letter_comp= [ l for l in "human"]
# print(h_letter_comp)

# # ___________________________________________________

# name = 'Andreja'
# for n in name:
#     print(n)

    
# new_name =[]
# for n in name:
#     new_name.append(n)
# print(new_name)


# name_comp = [ n for n in name]
# print(name_comp)

# name_lambda = map(lambda n: n , name)
# print(list(name_lambda))

# # ___________________________________________________


# num_list = [0,1,2,3,4,5,6,7,8,9,10]

# even_list = []
# for n in num_list:
#     if n%2 == 0:
#         even_list.append(n)
# print(even_list)

# even_list2 = [ n for n in num_list if n%2 ==0]
# print(even_list2)

# # ___________________________________________________



# my_dict = {'name':'Kaja', 'surname':'Jovanovski', 'age': 11}
# my_dict2 = dict( name = 'Andreja', surname='Jovanovski', age =46)
# my_dict3 = dict({ 'name':'Radica', 'surname': 'Jovanovski', 'age':40})
# my_dict4 = dict ([('name','Andreja' ), ('surname','Jovanovski'),('age',43)])

# print("**********************************************************************")
# print(my_dict)
# print(my_dict2)
# print(my_dict3)
# print(my_dict4)
# print("**********************************************************************")
# print(my_dict.keys())
# print(my_dict2.values())
# print(my_dict3.items())
# print("**********************************************************************")
# print(my_dict['name'])
# print(my_dict2['surname'])
# print("**********************************************************************")
# for k in my_dict.keys():
#     print(k)
# print()
# for v in my_dict2.values():
#     print(v)
# print()
# for k,v in my_dict3.items():
#     print(f"{k}: {v}")
# print("**********************************************************************")
# print("Andreja" in my_dict2.values())
# print('prezime' in my_dict.keys())
# print("**********************************************************************")
# print(my_dict2.get('surname'))
# print(my_dict.get('name'))
# print("**********************************************************************")
# dict4 = dict.fromkeys(['email',"password",'address'], 'NONE')
# print(dict4)

# list=[ 'name', 'surname', 'age']
# value = "TEST"
# dict5 = {}.fromkeys(list, 'NONE')
# print(dict5)

# dict6 = {}.fromkeys(list,value)
# print(dict6)

# value1 = [1]
# dict6 = {}.fromkeys(list,value1)
# print(dict6)
# value1.append([2,3])
# print(dict6)
# value2 = [2]
# dict6 = {}.fromkeys(list,value2)
# print(dict6)
# value2.extend([2,3,4])
# print(dict6)
# print("**********************************************************************")
# list_num = ( 0,1,2,3,4,5)
# square ={}

# for x in list_num:
#      square[x]=x*x
# print(square)

# square_com = { x:x*x for x in list_num}
# print(square_com)

# even_square = { x:x*x for x in range(13) if x%2 == 0}
# print(even_square)


# even_odd = { x: x*x if x%2 == 0 else 'odd' for x in range(13)}
# print(even_odd)

# def hello(name):
#     return f"Hello {name}"

# print(hello('Andreja'))

# def hi( name, surname):
#     return f"Hello {name} {surname}"

# print(hi("Andreja", "Jovanovski"))
# print(hi( surname='Jovanovski', name="Andreja"))

# def hi2(name , surname="Mitrovski"):
#     return f"Hello {name} {surname}"
# print(hi2("Andreja"))
# print(hi2("Andreja", "Jovanovski"))


# def show ( **kwargs):
#         #return kwargs
#         for key in kwargs:
#             print(f"{key}:{kwargs[key]}")
    
# #print(show(color='red',ID="101",language="Macedonian"))
# show(color='red',ID="101",language="Macedonian")


# names = { "first": "Andreja", "second": "Jovanovski"}
# def display_names(first,second):
#     return f"{first} say hello to {second}"
# print(display_names(**names))

# #word = 'abcddcba'
# word = "andreja"
# d = dict()

# for c in word:
#     if c not in d:
#         d[c]=1
#     else:
#         d[c] = d[c]+1
# print(d)
    
# def multiple_letter_count(string):
#     return {letter:string.count(letter) for letter in string }
# print(multiple_letter_count("andreja"))
# print(multiple_letter_count("abcabcbca"))



# def num():
#     return '1' ,'2','3','4'

# print(type(num()))

# a,b,c,d = num()
# print([f"a = {a}, b = {b}, c = {c}, d = {d}"])

# def double(x):
#     return x*2

# x =5
# print(x)
# x=double(x)
# print(x)

# def double_list(x):
#     double_num =[]
#     for i in x:
#         double_num.append(i*2)
#     return double_num

# a = [1,2,3,4,5]
# print(double_list(a))


# def double_list(x):
#      r = []
#      for i in x:
#          r.append(i * 2)
#      return r
 
# a = [ 6,7,8,9,10]
# print(double_list(a))

# def f(*args):
#   for x in args:
#       print(x)
 
# a = (1,2,3)
# b  = ('Andreja', "Radica", "Kaja")
# f(a)
# f(*a)
# f(b)
# f(*b)

# def f(**kwarg):
#     print(kwarg)
    
# f(a=1,b=2,c=3)

# list_dict = [ {'name':'Andreja', 'surname':'Jovanovski', 'age':45},{'name':'Radica', 'surname':'Jovanovski', 'age':40},
#              {'name':'Kaja', 'surname':'Jovanovski', 'age':11}]

#print(type(list_dict))

# print(list_dict)
# print(list_dict[0])
# print(type(list_dict[0]))
# print(list_dict[0]['name'])

# for d in list_dict:
#     for x in d:
#         print(d.get('name'))
#         break


# def f(fx):
#     print('fx =', fx, '/ id(fx) = ', id(fx))
#     fx = 10
#     print('fx =', fx, '/ id(fx) = ', id(fx))
    
# x = 5
# print('x =', x, '/ id(x) = ', id(x))

# f(x)

# print('x =', x, '/ id(x) = ', id(x))


# def f(x):
#     x[0] ='Andreja'
#     x[2]= '*****'


# my_list = ['foo', 'bar', 'baz', 'qux']
# print(my_list)
# f(my_list)
# print(my_list)

# def f(x):
#     x['foo']= '33'
#     x['baz'] = '****'


# my_dict = {'foo': 1, 'bar': 2, 'baz': 3}
# print(my_dict)
# f(my_dict)
# print(my_dict)


# def f():
#     return 'foo'

# s = f()
# s

# def double(x):
#     return x*2
    
# x=5
# x=double(x)
# # print(x)


# def f(*args):
#     print(type(args),args)


# f(1,2,3,4)

# def f(x,y,z):
#     print(f"{x},{y},{z}")
  
# t = [1,2,3]  
# f(*t)

# word = ['name', 'surname', 'age']
# # f(*word)

# def x(*args):
#     for i in args:
#         print(i)

# x(*word)

# def f(**kwargs):
#     print(kwargs)
#     for key,val in kwargs.items():
#         print(f"{key}:{val}")


# f(foo=1,bar=2,baz=3)

# def f1(**kwargs):
#     print(kwargs)


# def packing(*args):
#     print(type(args))
#     print(args)
#     for x in args:
#         print(x)
#         #for y in x:
#         #    print(y)
    
# packing(1,2,3)
# #packing([1,2,3])


# def unpacking(*t):
#      print(t)
#      for x in t:
#          print(x)
    

# t=('foo','baz', 'bar')
# unpacking(*t)




# number = [1,2,3,4,5]
# square =[]

# for num in number:
#     square.append(num**2)
# print(square)



# def square1(num):
#     return num**2

# square2 = map (square1,number)
# print(list(square2))

from imaplib import IMAP4_stream


participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]

def sorter(item):
    error1 = 100 -item[1]
    age = item[2]
    return  error1,age
    
    
sorted_list= sorted(participant_list, key =sorter)
print(sorted_list)