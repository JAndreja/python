import random
random_number = random.randint(1,10)
user_number = None
while user_number != random_number:
    user_number =int(input("Pick a number between 1 and 10: "))
    if user_number > random_number:
        print("Too high, try again!")
    elif user_number < random_number:
        print("Too low, try again!")
    else:
        print("YOU WON!!!")
