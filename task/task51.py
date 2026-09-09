""" Write a Python program to create a simple password validation system.
The program should repeatidly ask the user to enter a password until a valid password is entered. A password will be considered valid only if it has at least 8 character and contains the @ symbol
Once the user enters a valid password, the program should display"Password accepted"
and stop . Otherwise,it should display "Weak password .Try again" and ask for the password again.
"""
password = input("Enter the password : ")
while len(password) < 8 or '@' not in password:
    print("Weak Password. Try again")
    password = input("Etner the password: ")
print("Correct Password !")
