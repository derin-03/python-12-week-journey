while True:
    print("""Choose operations: 
    1. Addition (+)
    2. Subtraction (-)
    3. Multiplication (*)
    4. Division (/) 
    5. End program""")
    choice=input("Enter choice: ")
    if choice=="5":
        print("End program")
        break
    
    #Get input from user
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
        
    if choice=='1':
        print("Result:", num1+num2)
    elif choice=='2':
        print("Result:", num1-num2)
    elif choice=='3':
        print("Result:", num1*num2)
    elif choice=="4":
        if num2==0:
            print("Error; cannot be divided by 0")
        else:
            print("Result:", num1/num2)
    else:
        print("Invalid input")