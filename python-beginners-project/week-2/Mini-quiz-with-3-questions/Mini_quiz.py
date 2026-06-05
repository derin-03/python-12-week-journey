score=0
print("Q1: What is the capital of Nigeria?")
answer=input("Your answer: ")
if answer.strip().lower()  == "abuja":
    score+=1
print("Q2: What is the capital of Oyo State?")
answer=input("Your answer: ")
if answer.strip().lower() == "ibadan":
    score+=1
print("Q3: What is 5x6?")
answer=input("Your answer: ")
if answer.strip().lower() == "30":
    score+=1
print("Total:",score)

if score == 3:
    print("Excellent")
elif score == 2:
    print("Good")
elif score == 1:
    print("Poor")
else:
    print("Try again")