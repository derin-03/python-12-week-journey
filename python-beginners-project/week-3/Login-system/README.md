# Login System (3 Attempts Version)

## Algorithm
1. Start program
2. Store correct username and password
3. Set attempt counter to 0
4. Allow user to enter username and password
5. Compare input with stored credentials
   - If correct → display "Login successful" and stop program
   - If incorrect → increase attempt counter
6. Display remaining attempts after each failed login
7. If attempts reach 3 → lock system and stop program
8. End program

## Description
This is a simple Python login system that simulates user authentication. It allows a maximum of 3 login attempts before locking the system.

## ⚙️ Features
1. Username and password authentication
2. Maximum of 3 login attempts
3. Attempt tracking system
4. Success and failure messages
5. System lock after failed attempts

## Concepts Used
1. Variables
2. User input
3. Conditional statements (`if / else`)
4. Loops (`while`)
5. Counters
6. String comparison
7. f-strings

## How to Run
1. Open project in VS Code
2. Run `login_system.py`
3. Enter username and password
4. Try logging in (max 3 attempts)
5. View result message

## Source Code
All code is in `login_system.py` inside this repository.

## What I Learned
1. How authentication systems work
2. How to limit user attempts
3. How to use loops for repeated login attempts
4. How to control program flow using conditions
5. How to build basic security logic in Python

## Future Improvements
1. Add password masking (hidden input)
2. Add case-insensitive username handling
3. Add password reset option
4. Add login delay after failed attempts
5. Store multiple users instead of one
