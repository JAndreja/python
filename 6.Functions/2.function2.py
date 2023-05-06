# *args PACKING  A special operator we can pass to functions.Gathers remaining arguments as a tuple


def sum_all_num(*nums):
    total =0
    for num in nums:
        total += num
    return total

print(sum_all_num(1,2,3))
print(sum_all_num(2,12))

print("-------------------")

def ensure_correct_info(*args):
    if "Colt" in args and "Steele" in args:
        return "Welcome back Colt!"
    return "Not sure who you are..."

print(ensure_correct_info("test", False))
print(ensure_correct_info(1, True, "Steele", "Colt"))
print("-------------------")

# **kwargs PACKING  Gathers remaining keyword arguments as a dictionary

def fav_colors(**kwpeople):
    #print(kwpeople)
    for name , color in kwpeople.items():
        print(f"{name}'s favorite color is {color}")
    
fav_colors(Andreja="green",Radica="blue",Kaja="red")
fav_colors(Andreja="green",Radica="blue",Kaja="red", Maza="yellow")
print("-------------------")

def special_greeting(**kwargs):
    if "Andreja" in kwargs and kwargs["Andreja"] == "special":
        return "You get a special greeting Andreja!"
    elif "Andreja" in kwargs:
        return f"{kwargs['Andreja']} Andreja!"
    return "Not sure who this is..."

print(special_greeting(Andreja='Helloooo'))
print(special_greeting(Bob='hello'))
print(special_greeting(Andreja='special'))
print("-------------------")


#Parameter Ordering
 #   parameters
 #   *args
 #   default parameters
 #   **kwargs

def display_info(a,b,*args, tester="andreja",**kwargs):
     return [a,b,args,tester,kwargs]
 
print(display_info(1, 2, 3, last_name="Steele", job="tester"))
print("-------------------")

# Using * as an Argument: Argument Unpacking

def sum_all_values(*args):
    print(args)
    total=0
    for num in args:
        total += num
    print(total)

#sum_all_values(1,30,20,10)
nums=[1,2,3,4,5,6]
print(type(nums))
nums1=(1,2,3,4,5,6)
print(type(nums1))
sum_all_values(*nums)
sum_all_values(*nums1)
print("-------------------")

# Using ** as an Argument:Dictionary Unpacking .We can use ** as an argument to a function to "unpack" dictionary values into keyword arguments

def display_names(first,second):
    return f"{first} say hello to {second}"

names = { "first": "Andreja", "second": "Jovanovski"}

print(display_names(**names))

print("-------------------")


def add_num_multiply_num(a,b,c):
    print(a+b*c)

data = dict(a=1,b=2,c=3)
#add_num_multiply_num(data)
add_num_multiply_num(**data)