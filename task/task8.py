""" Write a Pyhton program to calculate Simple interest and total amount using Principal, Rate, and time entered by the user. """

P = int(input("Enter Principal Amount: "))
R = int(input("Enter Rate: "))
T = int(input("Enter Time: "))
SI = P*R*T/100
print("Simple Interest : ",SI)
print("Total Amount : ",SI+P)