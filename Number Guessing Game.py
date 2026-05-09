import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    attempts = 0  # Track the number of attempts

    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100.")

    while True:
        # Get user's guess
        user_guess = int(input("Enter your guess: "))
        attempts += 1  # Increment attempts count

        # Check if the guess is correct
        if user_guess < random_number:
            print("Too low! Try again.")
        elif user_guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {random_number} correctly!")
            print(f"It took you {attempts} attempts.")
            break  # Exit the loop if the guess is correct

# Start the game
number_guessing_game()
