import random

def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    print("Welcome to Rock-Paper-Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play, or 'quit' to exit.")

    while True:
        user_choice = input("Enter your choice: ").lower()
        if user_choice == "quit":
            print("Thanks for playing! Goodbye!")
            break

        if user_choice not in options:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue

        if user_choice == computer_choice:
            print("It's a tie!")
            print(f"Computer also chose {computer_choice}.")
        elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") and (user_choice == "scissors" and computer_choice == "paper"):
            print("Congratulations! you win!")
            print(f"Computer chose {computer_choice}.")
        else:
            print("Sorry, you lost. Better luck next time!")
            print(f"Computer chose {computer_choice}.")

        print()
        computer_choice = random.choice(options)

# Run the game
rock_paper_scissors()