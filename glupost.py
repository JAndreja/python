#num1 = float(input("Vnesete go prviot broj: "))
#num2 = float(input("Vnesete go vtoriot broj: "))
#sum = num1 + num2
#print(f"{sum}")


#name = input("Vnesete go vasheto ime: ")

#if name == "Andreja":
#    print(f"Hello {name}")
#else:
#    print(f"Sorry {name}, you are not Andreja.I'm sad")


# value_if_true if condition else value_if_false

#print(f"Hello {name}") if name == "Andreja" else print(f"Sorry {name}, you are not Andreja.I'm sad")


#command = ''

#while command.lower() != 'quit':
#    command = input('> ')
#print(f"You enter {command} and quit the loop")

#password = input("Enter password: ")

#while password.lower() != "familija":
#    password = input("Please enter the correct password: ")
#print("Your password is correct, Welcome!!!")


for x in range(5):
    for y in range(5):
        # terminate the innermost loop
        if y > 2:
            break
        # show coordinates on the screen
        print(f"({x},{y})")


name = "Andreja"

print(name[0].lower())
new_upper_name = name.upper()
print(new_upper_name)

new_name = []
for c in name:
    new_name.append(c.upper())
print(new_name)