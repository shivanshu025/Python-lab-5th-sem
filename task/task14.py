""" Write a python program to take an amount in rupees and calculate how many $500 and $100 notes are needed"""

n = int(input("Enter the amount: "))
note500 = n//500
note100 = (n%500)//100
print(f"500 notes: {note500} , 100 notes: {note100}")