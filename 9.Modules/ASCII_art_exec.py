from pyfiglet import figlet_format
from termcolor import colored
from colorama import init
init()

def print_art( msg, color):
    valid_color=("red", "green", "yellow", "blue", "magenta", "cyan", "white")
    if color not in valid_color:
        color="blue"
    ascii_art = figlet_format(msg)
    colored_ascii = colored(ascii_art, color=color)
    return colored_ascii
    
msg = input("What would you like to print? ")
user_color = input("What color? ")
print(print_art(msg,user_color))