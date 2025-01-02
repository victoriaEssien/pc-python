import random

print("Welcome to my Guessing Game!")
print("I'm thinking of a number from 1 - 100")
print("Can you guess it?")

number_to_guess = random.randint(1, 100)
user_guess = int(input("Enter a number between 1 and 100: "))

if number_to_guess > user_guess:
    print("Too low! Try again.")
    print(f"The number is {number_to_guess}")
elif number_to_guess < user_guess:
    print("Too high! Try again.")
    print(f"The number is {number_to_guess}")
elif number_to_guess == user_guess :
    print("Congratulations! You guessed the number correctly.")
else :
    print("Invalid input. Please enter a number between 1 and 100.")