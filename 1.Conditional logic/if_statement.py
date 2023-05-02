name=input("Please enter your name: ")

if name == "Andreja":
    print(f"Hello {name}")
elif name == "Radica":
    print(f"Hello {name}")
else:
    print(f"Sorry {name}, you are not Andreja")


name = input("Vnesete go vasheto ime: ")

if name == "Andreja":
    print(f"Hello {name}")
else:
    print(f"Sorry {name}, you are not Andreja.I'm sad")


      ## ternary operator ## 
########################################################
#  [value_if_true] if condition else [value_if_false]  #
########################################################

print(f"Hello {name}") if name == "Andreja" else print(f"Sorry {name}, you are not Andreja.I'm sad")