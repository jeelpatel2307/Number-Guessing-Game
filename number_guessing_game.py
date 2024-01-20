import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Set the initial number of attempts
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100. Try to guess it.")

    while True:
        # Get the player's guess
        guess = int(input("Enter your guess: "))
        
        # Increment the number of attempts
        attempts += 1
        
        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Try again. The correct number is higher.")
        else:
            print("Try again. The correct number is lower.")

if __name__ == "__main__":
    # Run the game
    number_guessing_game()
