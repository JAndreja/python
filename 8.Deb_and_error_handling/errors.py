#SyntaxError
#NameError
#TypeError
#IndexError
#ValueError
#KeyError
#AttributeError

# RAISE YOUR OWN EXCEPTION!!!!!

#def colorize(text, color):
#   colors = ( "red", "green", "yellow", "blue")
#   if type(text) is not str:
#      raise TypeError("TEXT MUST BE A STRING")
#   if color not in colors:
#      raise ValueError("color is invalid color")
#   print (f"printed {text} in {color}")
#colorize("hello", "red")
#colorize( 5, "red")
#colorize("hello", "magenta")


# HANDLE ERRORS
# THE BASIC SYNTAX:
# try:
# except:

def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None
d = {"name": "Ricky"}
print(get(d, "city"))
print(get(d, "name"))