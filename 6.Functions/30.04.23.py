def say_hi():
    print("Hi!")

say_hi()


def sum():
    return 9+9
results = sum()
print(results)


def multi():
    return 3*3
print(multi())


from random import randint
def check():
    r = randint(1,30)
    if r > 15:
        return f'number is {r}: BOOM'
    else:
        return f'number is {r}: AHHHH'
print(check())


result = []
def generate_evens():
    for x in range(1,50):
        if x % 2 == 0:
            result.append(x)
    return result
print(generate_evens())


def say_hi(name, surname):
    print(f"Hi {name} {surname}")

say_hi("Andreja" , "Jovanovski")

def square(num):
    return num*num
print(square(4))
print(square(8))
square_of_10 = square(10)
print(square_of_10)


def sum(a,b):
    return a+b  

def mult(c,d):   
    return c*d   

def sum_of_all(a,b,c,d):
    result = sum(a,b) + mult(c,d)
    return result

def sum_of_all_2(a,b):
    return sum(a,b) +mult(a,b)

def sum_of_all_3(a,b):  
    return a + b

print(sum_of_all(2,8,2,5))
print(sum_of_all_2(2,8))
print(sum_of_all_3(sum(2,8),mult(2,5)))