import random
random_number = random.randint(1,10)
user_number = None
while True:
    user_number =int(input("Pick a number between 1 and 10: "))
    if user_number > random_number:
        print("Too high, try again!")
    elif user_number < random_number:
        print("Too low, try again!")
    else:
        print("YOU WON!!!")
        play_again = input("Do you want to play again? (y/n)")
        if play_again == "y":
            random_number = random.randint(1,10)
            user_number = None
        else:
            print("Thank you for playing!")
            break

