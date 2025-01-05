import random

print("Welcome to Rock-Paper-Scissors!")
print("Type 'rock', 'paper', or 'scissors' to play, or 'quit' to exit.")

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
user_choice = input("Enter your choice: ")

if user_choice == computer_choice:
    print("It's a tie!")
    print(f"Computer also chose {computer_choice}.")
elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") and (user_choice == "scissors" and computer_choice == "paper"):
    print("Congratulations! you win!")
    print(f"Computer chose {computer_choice}.")
else:
    print("Sorry, you lost. Better luck next time!")
    print(f"Computer chose {computer_choice}.")
