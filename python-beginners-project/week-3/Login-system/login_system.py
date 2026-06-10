correct_username = "aderinsola"
correct_password = "derin"

print("=== LOGIN SYSTEM ===")

attempt = 0
max_attempts = 3

while attempt < max_attempts:
    username = input("Username: ")
    password = input("Password: ")

    if username == correct_username and password == correct_password:
        print("Login successful")
        break
    else:
        attempt += 1
        remaining = max_attempts - attempt

        if remaining > 0:
            print(f"Invalid login. You have {remaining} attempt(s) left.")
        else:
            print("No more attempts. Account locked.")