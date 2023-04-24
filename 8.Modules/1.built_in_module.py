import random

print(random.choices(["blue","red","green","yellow"]))

# reference to random with some other name
import random as r

print(r.randint(1,6))
print(r.choice(["blue","red","green","yellow"]))

# import parts of module
from random import choice,randint

print(choice(["blue","red","green","yellow"]))
print(randint(1,100))
print()
#*****************************
# exercise 

import keyword

def contains_keyword(*args_list):
    for args in args_list:
        if keyword.iskeyword(args):
            return True
    return False    
print(contains_keyword("hello", "goodbye"))
print(contains_keyword("def", "haha","lol","alaska"))

#*****************************