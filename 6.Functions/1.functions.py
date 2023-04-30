#function structure

# def name_of_function():
       # block of runnable code

#first function 

def say_hi():
    print('Hi!')

say_hi()

# Returning Values from Functions

def square_of_7():
    return 7**2
result= square_of_7()
print(result)

def name():
    return 'Andreja Jovanovski'
result= name()
print(result)
print(name())


# ****************************************************************************
#                 Parameters vs Arguments

#  A parameter is a variable in a method definition.
#  When a method is called, the arguments are the data you pass into the method's parameters.
#  Parameter is variable in the declaration of function.
#  Argument is the actual value of this variable that gets passed to function.

# ****************************************************************************

# function with paramethars 
# with one parameter
def hello_name(name):             # "name" here is called PARAMETER 
    return f"Hello {name}"
print(hello_name('Andreja'))      #  Here is called ARGUMENT

def square(x):
    return x*x
print(f"4 * 4 = {square(4)}")

# with two parametars
def sum(a,b):      # a i b are parameters
    print(f"{a} + {b} = {a+b}")

sum(2,4)    # 2,4 are arguments

# default parametars
# When you define a function and use an = you are setting a default parameter

def add(a=10, b=20):
    return a+b

print(add())
print(add(1,10)) 

def add1(a , b=1):
    return a+b

#print(add1())  # ne raboti bidejki ne e vnesen vrednost za a
print(add1(2))

# KEYWORD ARGUMENTS
# When you invoke a function and use an = you are making a keyword argument

def full_name(first, last):
    return f"Your name is {first} {last}"

print(full_name(first='Andreja', last='Jovanovski')) 
print(full_name(last='Jovanovski', first='Andreja'))

# Scope

name = 'Andreja'

def say_hello():
    return f'Hello {name}'
print(say_hello())

def say_hello1():
    name1 = 'Andreja'
    return f'Hello {name1}'
print(say_hello1())
#print(name1)  #(name1) # NameError

# Global 

total = 0
def increment():
    global total
    total += 1
    return total

print(increment())

# nonlocal

def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner()

print(outer())