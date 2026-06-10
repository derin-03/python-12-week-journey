import random
secret_number=random.randint(1, 10)
count=0
print("Guess a number between 1 and 10")
while True:
    guess=int(input("Enter guessed number: "))
    count+=1
    if guess<secret_number:
        print("Too low")
    elif guess>secret_number:
        print("Too high")
    else:
        print("correct")
        break
print("Weldone!")
print(f'you guessed it in {count} attempts.')