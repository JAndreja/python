# ** all **
# Return True if all elements of the iterable are truthy (or if the iterable is empty)

list1=all([1,2,3,4,5])
list2=all([0,1,2,3,4])

print(list1)
print(list2)

num = [4,2,6,10,8]

even_num=[n for n in num if n %2 == 0]
print(all(even_num))

people = ["Andreja", "Angel", "aneta", "Andrijana"]
without_all=[name[0].upper() == 'A' for name in people]
print(without_all)
with_all=all([name[0].upper() == 'A' for name in people])
print(with_all)

print( "***********************************************************************")

# ** any **
# Return True if any element of the iterable is truthy. If the iterable is empty, return False. 

people = ["Andreja", "Kaja", "Radica", "maza"]
with_any=any([ name[0] == 'A' for name in people])
print(with_all)

num = [0,1,2,3]
without_any1 = [ n for n in num if n > 2]
print(without_any1)
num_any = any ([ n for n in num if n > 2])
print(num_any)

# new_str_list = []
# def is_all_strings(str_list):
#     for s in str_list:
#         if type(s) == str:
#             new_str_list.append(s)
#     print(new_str_list)
# is_all_strings([2,'a','b','c'])


def is_all_string(list):
    return all([type(s) == str for s in list ])

print(is_all_string([2,'a','b','c']))
print(is_all_string(['a','b','c']))
print(is_all_string(['andreja','radica','c']))

print("***********************************************************************")

#  ** sorted **
# Returns a new sorted list from the items in iterable

#list
list_numbers= [ 2,1,6,4,3]
print(sorted(list_numbers))

#tuple
tuple_num = ( 2,3,1,9,4,8,5)
print(sorted(tuple_num))

print("***********************************************************************")

# ** max **
# Return the largest item in an iterable or the largest of two or more arguments.

num_list = [ 3,4,66,1,98,33]
char_list = ['a', 'd', 'b', 'e']
print(max(num_list))
print(max(char_list))

print("***********************************************************************")
      
#  ** min **
# Return the smallest item in an iterable or the smallest of two or more arguments.

num_list = [ 3,4,66,1,98,33]
char_list = ['a', 'd', 'b', 'e']
print(min(num_list))
print(min(char_list))

names= [ 'Arya', 'Samson', 'Dora','Tim', 'Ollivander' ]

min_list=min([len(name) for name in names])
print(min_list)

# To customize the sort order key parameter is passed in the min() function. 
print(min(names, key=lambda n: len(n))
      )

print("***********************************************************************")
print("***********************************************************************")
# exercise min max
 
def extreme(iterable):
      return (min(iterable),max(iterable))

print(extreme([1,2,3,4,5]))
print(extreme('alcatraz'))
print(extreme((-99,25,0,-7,44)))

# *********************************************************************

print("***********************************************************************")

# ** reversed **
# Return a reverse iterator. 

nums = [1,2,4,8,2,5]
string_name =("hello Andreja")

print(list(reversed(nums)))
print(list(reversed(string_name)))

print("***********************************************************************")

# ** len ** 
#Return the length (the number of items) of an object. The argument may be a #sequence (such as a string, tuple, list, or range) or a collection (such as a #dictionary, set)

print("***********************************************************************")

# abs
# Return the absolute value of a number. The argument may be an integer or a 
#  floating point number.

num = (5)
num1 = (-5)
print(abs(num))
print(abs(num1))

print("***********************************************************************")

# ** sum **
# Takes an iterable and an optional start.
# Returns the sum of start and the items of an iterable from left to right and # returns the total.
#start defaults to 0

nums = [1,3,4,5]
nums_with_start = [1,3,4,5]
print(sum(nums))
print(sum(nums_with_start,10))

print("***********************************************************************")


#  ** round **
# Return number rounded to ndigits precision after the decimal point. If #ndigits is omitted or is None, it returns the nearest integer to its input.

print(round(10.2))
print(round(5.7))

print("***********************************************************************")
print("***********************************************************************")

# exercise

# exec 1
def max_magnitude(list_num):
    return max(abs(num) for num in list_num)
    
print(max_magnitude([300,30,-900]))

#exec2
# def sum_even_values(*nums):
#     sum_even= 0
#     for num in nums:
#         if num % 2 == 0:
#            sum_even += num
#     print(sum_even)
#     return 0
    
def sum_even_values1(*nums):
        return sum( num for num in nums if num %2 ==0)
    
#sum_even_values(1,2,3,4,5,6)
#sum_even_values(1,3,5)
print(sum_even_values1(2,4,6,8,1))
print(sum_even_values1(1,3,5))

#exec3

def sum_floats(*args):
    return sum( arg for arg in args if type(arg)== float)

print(sum_floats(1.5,2.4,'awesome',[],1))
print(sum_floats(1,2,3,4,5))

print("***********************************************************************")

# ** zip **
# Make an iterator that aggregates elements from each of the iterables.
#Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
#The iterator stops when the shortest input iterable is exhausted.

zip_number =zip([1,2,3],[4,5,6])
print(list(zip_number))
zip_dict =zip([1,2,3],["Andreja", "Radica","Kaja"])
print(dict(zip_dict))
# -------------------------------------------------------
midterm = [80,91,78]
finals = [98,89,53]
students = [ 'dan', 'ang', 'kate']
 # with zip
max_grades=[max(pair) for pair in zip(midterm, finals)]
final_grades=zip(students,max_grades)
print(dict(final_grades))


final_grades={pair[0]:max(pair[1],pair[2]) for pair in zip(students,midterm, finals)}
print(final_grades)

# with lambda

scores=zip(students,map(lambda pair: max(pair),zip(midterm,finals)))
#print(list(scores))
print(dict(scores))


print("***********************************************************************")
print("***********************************************************************")

# exercise

# exec 1

def interleave( str1, str2):
   join_str= []
   for x in zip(str1,str2):
       join_str.append(''.join(x))
   return ''.join(join_str)
   
def interleave1(str1 ,str2 ):
   return "".join("".join(x) for x in (zip(str1,str2)))
   
print(interleave('hi', 'ha'))
print(interleave('aaaa', 'zzzz'))

print(interleave1('hi', 'ha'))
print(interleave1('aaaa', 'zzzz'))

# exec 2


def triple_and_filter(list_nums):
    new_list =[]
    for num in list_nums:
        if num %4 ==0:
            new_list.append(num*3)
    return new_list
    
def triple_and_filter1(list_num):
    return list(( num*3 for num in list_num if num%4 ==0))

    
def triple_and_filter2(list_num):
    return list(filter(lambda x: x%4 ==0 ,map(lambda x: x*3, list_num)))

print(triple_and_filter([1,2,3,4]))
print(triple_and_filter([6,8,10,12]))


print(triple_and_filter1([1,2,3,4]))
print(triple_and_filter1([6,8,10,12]))


print(triple_and_filter2([1,2,3,4]))
print(triple_and_filter2([6,8,10,12]))

# exec 3

names = [{'first': 'Andreja', 'last': 'Jovanovski'}, 
         {'first': 'Radica', 'last': 'Mihajlovski'}
        ]


def extra_full_name(list_dict):
     new_list =[]
     for x in list_dict:
         new_list.append(x['first']  + ' '+ x['last'])
     return new_list

def extra_full_name1(list_dict):
     return list(map(lambda val: f"{val['first']} {val['last']}",names))

    
print(extra_full_name(names))
print(extra_full_name1(names))