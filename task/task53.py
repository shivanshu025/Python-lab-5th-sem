""" Write a Python program to input four numbers from the user and find the greatest number among them."""
for i in range(4):
    num = int(input("Enter number: "))
    if i == 0:
        greatest = num
    elif num > greatest:
        greatest = num
print("The greatest number is:", greatest)