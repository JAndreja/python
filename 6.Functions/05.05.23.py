def say_hi():
    print("Hi")

say_hi()


def sum():
    print(2+2)

sum()

def square_of_7():
    return 7*7

print(square_of_7())
res = square_of_7()
print(res)

def generate_evens():
    result =[]
    for x in range(1,51):
        if x%2 == 0:
            result.append(x)
    return result
print(generate_evens())


#x = int(input("Enter number: "))
#def sqaure(x):
#    return x*x
#print(sqaure(x))

#x = int(input("Enter first number: "))
#y = int(input("Enter second number: "))

#def add(x,y):
#    return x+y
#print(add(x,y ))

#name = input("Enter your name: ")
#surname = input("Enter your surname: ")

#def user_info(first,last):
#    return f"Hello {first} {last}"
#print(user_info(first = name, last = surname))


def fun1(a,b):
    return a+b   
def fun2(c,d):
    return c*d   
def math( a,b,c,d, fn1=fun1 , fn2=fun2):
    return fn1(a,b)*fn2(c,d)  
print(math(2,2,2,2))


def math2(a,b,c,d, fn = fun1):
    return fn(a,b)
print(math2(2,2,3,3))
print(math2(2,3,2,3, fun2))

def math3(fn1 = fun1 , fn2=fun2):
    return fn1 * fn2
print(math3(fun1(1,2),fun2(2,5)))
