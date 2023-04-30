# Define a function product that returns the product of two numbers:

def product(a,b):
    return a*b

print(product(2,2))

#Function takes is one parameter ( number from 1-7) and return the day of the week.If number is less than 1 or greater than 7 return None

def return_day(num):
    days = ["Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    if num > 0 and num <= len(days):
        return days[num-1]
    else:
        return None
print(return_day(2))
   
# This function takes in one paramether and returns the last value in the list.Return None if the list is empty

def last_element(list):
    if len(list) != 0:
        return list.pop()
    else:
        return None

print(last_element([1,2,3,5,6]))
print(last_element([]))

# This function takes in two parameters(numbers)If the first is greater than the second, this function return "First is greater".If the second is greater than the first , 
# the function returns "Second is greater".Otherwise the function return "Numbers are equal"

def number_compare(num1, num2):
    if num1 > num2:
        return f"{num1} > {num2}"
    elif num1 < num2:
        return f"{num1} < {num2}"
    else:
        return f"{num1} = {num2}"

print(number_compare(3,2))
print(number_compare(2,3))
print(number_compare(2,2))

#This function takes two parameters (strings).The first parameter should be a word and second should be a letter.
#The function returns the number of times that letter appears in the word.If the letter is not found in the word, the function should return 0

def single_letter_count( string , letter):    
         return string.lower().count(letter.lower())

print(single_letter_count("andreja" , "a"))

# This function takes in one parameter (a string) and returns a dictionary with keys being letters and the values being the count of the letter.

def multi_letter_count(string):
      return { letter.lower():string.count(letter.lower()) for letter in string}
print(multi_letter_count("Ananas"))


# This function should take in four parameters ( list,command, location and value)

def list_manipulation(list,command,location,value = None):
     if command == "remove" and location == "end":
          return list.pop()
     elif command == "remove" and location == "beginning":
          return list.pop(0)
     elif command == "add" and location == "beginning":
          list.insert(0,value)
          return list
     elif command == "add" and location == "end":
          list.append(value)
          return list
          
     
print(list_manipulation([1,2,3], "remove", "end"))
print(list_manipulation([1,2,3], "remove", "beginning"))
print(list_manipulation([1,2,3], "add", "beginning", 20))
print(list_manipulation([1,2,3], "add", "end", 30))


# This function accepts a list and a search_term and return the number the search_term appear in the list

def frequency(list , serach_term):
      return f"number {serach_term} apears: {list.count(serach_term)} times"

print(frequency([1,2,3,4,56,7,8,8,2,1,3,3], 3))


# This function accepts a list of numbers and return the product of all even number in the list

def multiply_even_numbers(list):
      product =1
      for num in list:
           if num %2 == 0:
                product *= num
      return product

print(multiply_even_numbers([2,3,4,5,6])) 

# This function accepts a string and returns the same string with the first letter capitalized.

def capitalize(word):
     return f"{word[0].upper()}{word[1:]}"

print(capitalize("andreja"))

#This function accepts a list and returns a list of values that are truthy values, without any of the falsey values

def compact(list):
    truthy = []
    for item in list:
         if item:
              truthy.append(item)
    return truthy

print(compact([0,1,2,"",[], False, {}, None, "All done"]))

# This function should accept two list and return a list with the values that are in both input list

def intersection(list1, list2):
     new_list =[]
     for l in list1:
          if l in list2:
               new_list.append(l)
     return new_list

print(intersection([1,2,3,4],[2,3,5,6]))



