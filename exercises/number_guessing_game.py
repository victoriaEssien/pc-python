import random

print("Welcome to my Guessing Game!")
print("I'm thinking of a number from 1 - 100")
print("Can you guess it? You have 4 attempts.")

number_to_guess = random.randint(1, 100)
attempts = 0
max_attempts = 4

while attempts < max_attempts:
    try:
        user_guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter a number between 1 and 100: "))
        if user_guess < 1 or user_guess > 100:
            print("Invalid input. Please enter a number between 1 and 100.")
            continue

        attempts += 1  # Increment attempts after a valid guess

        if number_to_guess > user_guess:
            print("Too low! Try again.")
        elif number_to_guess < user_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number correctly in {attempts} attempt(s).")
            break  # Exit the loop if the user guesses correctly
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if attempts == max_attempts and user_guess != number_to_guess:
    print(f"Sorry! You've used all your attempts. The number was {number_to_guess}.")
