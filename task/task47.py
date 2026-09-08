""" Take a password and check length, presence of @, and whether first and last characters are different."""
password = input("Enter password: ")
print(len(password) >= 8 and '@' in password and password[0] != password[-1])