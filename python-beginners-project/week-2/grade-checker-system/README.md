# Grade Checker System

## Algorithm
1. Start program
2. Ask user for score input
3. Convert input to number
4. Check if score is valid
   - If score is less than 0 or greater than 100:
     print "Invalid score"
5. Check grade range:
   - 70–100 → A
   - 60–69 → B
   - 50–59 → C
   - 45–49 → D
   - 40–44 → E
   - Below 40 → F
6. Display grade
7. End program

## Description
This is a Python grade checker program that determines a student's grade based on their score using conditional statements and comparison operators.

## Features
1. Accepts user score input
2. Validates score range
3. Displays grade based on score
4. Handles invalid score input

## Concepts Used
1. Variables
2. User input
3. Conditional statements
4. Comparison operators
5. Float conversion
6. Logical operators (`or`)

## How to Run
1. Open project in VS Code
2. Run `grade_checker.py`
3. Enter your score
4. View grade result

## 🔗 Source Code
All code is in `grade_checker.py` inside this repository.

## What I Learned
1. How to use if-elif-else conditions
2. How to validate user input
3. How ordered conditions work
4. How comparison operators are used in decision-making

## Future Improvements
1. Add GPA calculation
2. Allow multiple student scores
3. Display remarks alongside grades
4. Handle non-numeric input errors