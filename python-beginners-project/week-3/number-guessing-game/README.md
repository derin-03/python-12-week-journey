# Number Guessing Game

## Algorithm
1. Start program
2. Generate a random number between 1 and 10
3. Set attempt counter to 0
4. Ask user to guess a number
5. Increase attempt counter by 1
6. Compare guess with the secret number:
   - If guess is lower than the secret number, display "Too low"
   - If guess is higher than the secret number, display "Too high"
   - If guess is correct, display "Correct" and end the loop
7. Display the total number of attempts
8. End program

## Description
This is a simple Python number guessing game where the computer generates a random number between 1 and 10. The user keeps guessing until the correct number is found.

## Features
1. Generates a random secret number
2. Accepts user guesses
3. Provides hints when guesses are too high or too low
4. Tracks the number of attempts
5. Displays a success message when the correct number is guessed

## Concepts Used
1. Variables
2. User input
3. Integer conversion
4. Conditional statements (`if`, `elif`, `else`)
5. Loops (`while`)
6. Loop control (`break`)
7. Counters
8. Random number generation (`random.randint`)
9. f-strings

## How to Run
1. Open project in VS Code
2. Run `number_guessing_game.py`
3. Enter a guess between 1 and 10
4. Continue guessing until the correct number is found
5. View the total number of attempts

## Source Code
The source code is located in `number_guessing_game.py` in this repository.

## What I Learned
1. How to use the `random` module
2. How to generate random numbers
3. How to use loops to repeat actions
4. How to stop a loop using `break`
5. How to count user attempts using a counter variable
6. How to use f-strings to display variables in output

## Future Improvements
1. Allow users to choose a difficulty level
2. Add a maximum number of attempts
3. Add a replay option
4. Display a leaderboard or high score
5. Handle invalid inputs gracefully
6. Expand the guessing range (e.g., 1–100)
