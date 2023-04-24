from termcolor import colored
from colorama import init

 # use colorama to make termcolor work on Windows too
init()

text=colored("Hi there", color="red", on_color='on_yellow')
print(text)