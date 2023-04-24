# Define a function product that returns the product of two numbers:

def product(a,b):
    return a*b
print(product(2,2))
print(product(2,-2))

print("--------------------------------------------------")
print()

# Function takes is one parameter ( number from 1-7) and return the day of the week.If number is less than 1 or greater than 7 return None

def return_day(num):
   days = ["Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
   if num > 0 and num <= len(days):
       return days[num-1]
   return None
print(return_day(3))        
print()
print()

def return_day1(num):
    days= { 1:"Monday", 2:"Tuesday", 3:"Wednesday",4:"Thursday", 5:"Friday",6:"Saturday",7:"Sunday" }
    day = days.get(num)
    if day:
        return day

print(return_day1(0))
print(return_day1(1))
print(return_day1(2))
print(return_day1(3))
print(return_day1(4))
print(return_day1(5))
print(return_day1(6))
print(return_day1(7))
print(return_day1(8))

print("--------------------------------------------------")
print()

# This function takes in one paramether and returns the last value in the list.Return None if the list is empty

def last_element(list):
    # if len(list)==0:
    #     return None
    # else:
    #   return list.pop()
    
    if list:
        return list.pop()
    return None
print(last_element([2,54,67,3,4,45]))
print(last_element([]))

print("--------------------------------------------------")
print()
    
# This function takes in two parameters(numbers)If the first is greater than the second, this function return "First is greater".If the second is greater than the first , the function returns "Second is greater".Otherwise the function return "Numbers are equal"

def number_compare( num1 , num2):
    if num1 > num2:
        return f"First is greater: {num1} > {num2}"
    elif num1 < num2:
        return f"Second is greater: {num1} < {num2}"
    return f"Numbers are equal: {num1} = {num2}"

print(number_compare(2,3))
print(number_compare(67,3))
print(number_compare(5,5))

print("--------------------------------------------------")
print()

# This function takes two parameters (strings).The first parameter should be a word and second should be a letter.The function returns the number of times that letter appears in the word.If the letter is not found in the word, the function should return 0

def single_letter_count( string, letter):
        return string.lower().count(letter.lower())
print(single_letter_count("andreja","A"))
print(single_letter_count("andreja","z"))

print("--------------------------------------------------")
print()

# This function takes in one parameter (a string) and returns a dictionary with keys being letters and the values being the count of the letter.

def multiple_letter_count(string):
    return {letter:string.count(letter) for letter in string }

print(multiple_letter_count("awesome"))
print(multiple_letter_count("abccbadeffdetkr"))

print("--------------------------------------------------")
print()
# This function should take in four parameters ( list,command, location and value)

def list_manipuation(collection, command, location, value=None):
    if (command == 'remove' and location == 'end'):
         return collection.pop()
    elif ( command == 'remove' and location == 'beginning'):
        return collection.pop(0)
    elif ( command == 'add' and location == 'beginning'):
        collection.insert(0,value)
        return collection
    elif ( command == 'add' and location == 'end'):
        collection.append(value)
        return collection
print(list_manipuation([1,2,3],"remove","end"))
print(list_manipuation([1,2,3],"remove","beginning"))
print(list_manipuation([1,2,3],"add","beginning",20 ))
print(list_manipuation([1,2,3],"add","end",30 ))

print("--------------------------------------------------")
print()

# This function should take in on paramether and return true or false depending on whether is a palindrome. allow your function to ignore white spaces and capitalization.

def is_palindrome(string):
     return string == string[::-1]
print(is_palindrome('testing'))
print(is_palindrome('tacocat'))

def is_palindrome1(string):
    stripped=string.replace(" ","")
    return stripped == stripped[::-1]
print(is_palindrome1('a man a plan a canal panama'))

print("--------------------------------------------------")
print()

# This function accepts a list and a search_term and return the number the search_term appear in the list

def frequency(list,term):
    return list.count(term)

print(frequency([1,2,3,4,4,4],4))
    
print("--------------------------------------------------")
print()

# This function accepts a list of numbers and return the product of all even number in the list

def multiply_even_numbers(numbs):
    total = 1
    for num in numbs:
        if num % 2 == 0:
            total = total * num
    return total
print(multiply_even_numbers([2,3,4,5,6]))

print("--------------------------------------------------")
print()

# This function accepts a string and returns the same string with the first letter capitalized.

def capitalize(string):
    return string[:1].upper() + string[1:]

print(capitalize('andreja'))
print(capitalize('jamaica'))

print("--------------------------------------------------")
print()

# This function accepts a list and returns a list of values that are truthy values, without any of the falsey values

def compact(list):
    truthy = []
    for item in list:
        if item:
            truthy.append(item)
    return truthy
print(compact([0,1,2,"",[], False, {}, None, "All done"]))

print("--------------------------------------------------")
print()

# This function should accept two list and return a list with the values that are in both input list

def intersection(list1, list2):
    new_list =[]
    for l in list1:
        if l in list2:
            new_list.append(l)
    return new_list

def intersection1(list1, list2):
    return[ l for l in list1 if l in list2]

def intersection2(list1, list2):
    return[l for l in set(list1) & set(list2)]


print(intersection([1,3,2],[3,4,2]))
print(intersection(["a","b","c","d",],["f","a","d","g","b"]))

print(intersection1([1,3,2],[3,4,2]))
print(intersection1(["a","b","c","d",],["f","a","d","g","b"]))

print(intersection2([1,3,2],[3,4,2]))
print(intersection2(["a","b","c","d",],["f","a","d","g","b"]))

print("--------------------------------------------------")
print()

# This function accepts a list and a callback function.Function should iterate over each element in the list and invoke the callback function at each iteration

def isEven(num):
    return num % 2 ==0

def partition(list,fn):
    trues =[]
    false=[]
    for l in list:
        if fn(l):
             trues.append(l)
        else:
            false.append(l)
    return [ trues, false]        
    
print(partition([1,2,3,4], isEven))
print(partition([5,3,4,7,9,2], isEven))

print("--------------------------------------------------")
print()

#####   *ARGS   #########
# This function accept any number of arguments.It's should return TRUE if any of arguments are 'purple'.otherwise ,it's should return False

# def contain_purple(*choice):
#     for item in choice:
#         if item == 'purple':
#             return True
#     return False

def contain_purple(*choice):
    if "purple" in choice:
        return True
    return False


print(contain_purple(25,"purple"))
print(contain_purple(25,"purple", False,37))
print(contain_purple(25,"test", True, 67, "yellow"))
print(contain_purple("purple"))
print("--------------------------------------------------")
print()

#####   **пѕ KWARGS   #########

# This function accepts a single string called word and any number of additional key word arguments.If a prefix is provided, return the prefix followed by the word.If a suffix is provided, return the word followed by the suffix.If neither is provided, just return the word.

def combine_words(word,**kwargs):
    if "prefix" in kwargs:
        return kwargs["prefix"] + word
    elif "suffix" in kwargs:
        return word + kwargs["suffix"]
    return word
    
print(combine_words("Andreja", prefix="man"))
print(combine_words("Radica", suffix="women"))
print(combine_words("Kaja"))
print("--------------------------------------------------")
print()

#### # Using * as an Argument: Argument Unpacking ####

def count_sevens(*args):
    return args.count(7)

result=(count_sevens(1,4,7))
print(result)

nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]

result2=(count_sevens(*nums))
print(result2)
print("--------------------------------------------------")
print()

 # Using ** as an Argument
 ##### CODING EXERCISE 59 #######   teska i nejasna
 
 
 