import time
seconds=int(input("Enter time in seconds: "))
while seconds > 0:
    print(seconds)
    seconds -= 1
    time.sleep(1)
print("Times up")