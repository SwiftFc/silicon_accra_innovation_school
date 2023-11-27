import random

# Generate a random number between 1 and 100
computer_number = random.randint(1, 100)

# Initialize variables
attempts = 0
max_attempts = 10  # You can adjust the number of attempts
guessed_number = None

print("Welcome to the Number Guessing Game!")
print(f"Try to guess the computer's number between 1 and 100 in {max_attempts} attempts.")

while attempts < max_attempts:
    try:
        # Get user's guess
        user_input = input("Enter your guess: ")
        guessed_number = int(user_input)

        # Check if the guess is correct
        if guessed_number == computer_number:
            print(f"Congratulations! You guessed the number {computer_number} correctly in {attempts + 1} attempts.")
            break
        elif guessed_number < computer_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")

        attempts += 1

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if guessed_number != computer_number:
    print(f"Sorry, you've reached the maximum number of attempts. The correct number was {computer_number}.")

