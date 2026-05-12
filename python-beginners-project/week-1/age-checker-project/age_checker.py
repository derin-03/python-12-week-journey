#Start program
age=int(input("Enter your Age: "))
#check age range
if age<0:
    print("inavlid Age")
elif age<13:
    print("You're a Child")
elif age<20:
    print("You're a Teenager")
elif age<60:
    print("You're an Adult")
else:
    print("You're a Senior")
#End program