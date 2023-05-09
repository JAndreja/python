import random
print(random.choices(["blue","red","green","yellow"]))
print(random.choice((1,2,3,45,6,7)))

import math 
print(math.sqrt(15129))

import math as sqrt
print(sqrt.sqrt(15129))

from math import sqrt
print(sqrt(15129))


import keyword
def contains_keyword(*arg_list):
    for args in arg_list:
        if keyword.iskeyword(args):
            return True
    return False

print(contains_keyword("hello", "goodbay"))
print(contains_keyword("def", "haha","lol","alaska"))


import bananas
import apples

print(bananas.deep_in_chocolate())
print(bananas.peel())
print(bananas.seel())
print(apples.bake())
print(apples.offer())

import termcolor
import colorama
colorama.init()

#print(dir(termcolor))
#print(help(termcolor))
text = (termcolor.colored("ZDRAVO ANDREJA", color ='magenta',on_color='on_cyan', attrs=["blink",'underline','bold']))
print(text)