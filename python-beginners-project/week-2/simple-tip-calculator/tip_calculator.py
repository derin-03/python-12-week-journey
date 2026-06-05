bill=float(input("Enter your bill amount:"))
tip_percentage=float(input("Enter tip percentage:"))
tip_amount=(tip_percentage/100)*bill
total_bill=tip_amount+bill
print("Bill Amount:",bill)
print("Tip percentage:",tip_percentage)
print("Tip Amount:",tip_amount)
print("Total bill:",total_bill)