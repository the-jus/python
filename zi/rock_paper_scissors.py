# importing random module
import random

choice = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
c_choice = random.choice(possible_actions)
print(f"\nYour choice =  {choice}, Computer's choice = {c_choice}.\n")

if choice == c_choice:
    print(f"Both players selected {choice}. It's a tie!")
elif choice == "rock":
    if c_choice == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif choice == "paper":
    if c_choice == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif choice == "scissors":
    if c_choice == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
