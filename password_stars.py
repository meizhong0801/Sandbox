MINIMUM_LENGTH = 8
password = input("Enter your password: ")
while len(password) < MINIMUM_LENGTH:
    print("The password length is too short")
    password = input("Enter your password: ")
print("*" * len(password))
