import random
from tkinter import W
players_wins = 0
computer_wins =0
winning_score = 2

while players_wins < winning_score and computer_wins < winning_score:
    print(f"*Player Score: {players_wins}\n*Computer Score: {computer_wins}")
    print("...rock...")
    print("...paper...")
    print("...scissors...")

    player=input("Player, make your move: ").lower()
    if player == "quit" or player == "q":
        break
    rand_num = random.randint(0,2)

    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else: 
        computer = "scissors"
    print(f"Computer plays: {computer}")
    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("player wins!")
            players_wins += 1
        elif computer == "paper":
            print("computer wins!")
            computer_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("player wins!")
            players_wins += 1
        elif computer == "scissors":      
            print("computer wins!")
            computer_wins += 1
    elif player == "scissors":
        if computer == "paper":
            print("player wins!")
            players_wins += 1
        elif computer == "rock":
            print("computer wins!")
            computer_wins += 1       
    else:
        print("Please enter valid move")
if players_wins > computer_wins:
    print("CONGRATS, YOU WON!")
elif players_wins == computer_wins:
    print("IT'S A TIE")
else:
    print("SORRY...COMPUTER WON!!")

