# Number Guessing Game

Welcome to the Number Guessing Game! This simple console-based game allows players to guess a randomly generated number between 1 and 100.

## How to Play

1. Run the script.
2. The program will generate a random number between 1 and 100.
3. Enter your guess when prompted.
4. Receive hints about whether your guess is higher or lower than the correct number.
5. Keep guessing until you correctly identify the number.

## Getting Started

### Prerequisites

Make sure you have Python installed on your machine.

### Running the Game

```bash
python number_guessing_game.py
```

Follow the on-screen instructions to play the game.

## Code Explanation

### `number_guessing_game()` Function

- Generates a random number as the correct answer.
- Initializes the number of attempts.
- Guides the player through the guessing process.
- Provides hints for higher or lower guesses.
- Congratulates the player upon correct guess.

### Running the Game

The game is executed by calling the `number_guessing_game()` function.

```python
if __name__ == "__main__":
    number_guessing_game()
```

## Author

Jeel Patel
