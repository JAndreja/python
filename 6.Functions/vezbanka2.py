
def test():
    return 'Andreja'

print(test())

def test(name):
    print("Hello ", name)

test("Andreja")

def sum_num( num1, num2):
    #return num1+num2
    print(f"{num1} + {num2} = {num1+num2}")
    
#print(sum_num(2,3))
sum_num(2,3)

def add( a=10,b=20):
    return a+b

print(add())
print(add(2,3))

def multi(a , b=4):
    return a*b

print(multi(5))

name= "Andreja"

def say_hello():
    name = "andreja"
    return f'Hello {name}'

print(say_hello())
print(f'Hello {name}')


def strings(*words):
    return " ".join(words)
print(strings("Andreja", "Jovanovski"))


def math(*nums):
    total =1
    for num in nums:
        total *= num
        num +=1
    return total

print(math(5,5,5))

def check_num(*numbers):
    if 5 in numbers and 6 in numbers:
        return "Yours lucky number is in list"
    return "Sorry, your lucky number is not in list"

print(check_num(1,2,5,6,7,8,9,10))
print(check_num(1,2,3,4))

def check_num1(*numbers1):
    for num in numbers1:
        if num ==5:
            print(f"Yours lucky number {num} is in list")
        else:
            print(f"Sorry, {num} is not your lucky number")

check_num1(1,2,6,5,7,8,9,10)

def fav_color(**kwpeople):
    #print(kwpeople)
    for k ,v in kwpeople.items():
        print(f"{k} favorite color is {v}")
        
fav_color(Andreja="green", Radica="blue", Kaja="red")

def fav_color1(**people):
      print(people)
      print(type(people))       
fav_color1(Andreja="green", Radica="blue", Kaja="red", a="1")


def greeting(**name):
    if "Andreja" in name and name["Radica"] == "Test":
        return "Hello Andreja and Radica"
    elif "Radica" in name and name["Andrejaa"] != "ello" :
        return "Hello Radica"
    return "Who are you???"
print(greeting(Andreja="hello" , Radica="Test"))
print(greeting(Andrejaa="hello" , Radica="Test"))
print(greeting(Andrejaa="ello" , Radica="Test"))

def sum(*nums):
    total = 0
    for num in nums:
        total += num
    return total
    

nums1=[1,2,3,4]
print(type(nums1))
nums2 = (1,2,3,4)
print(type(nums2))
print(sum(*nums1))
print(sum(*nums2))

def display_name(**name):
    print(name)
    
name=dict( name= "Andreja" , surname="Jovanovski")
display_name(**name)

def display_name1( first, second):
    return f"Hello {first} {second}"

name1=dict( first= "Radica" , second="Jovanovski")
print(display_name1(**name1))