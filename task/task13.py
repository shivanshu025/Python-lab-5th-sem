""" Write a python program to take a 2-digit number as input ans print the sum of its  digits """

n = int(input("Enter a 2-digit number: "))
sum = n%10
n//=10
print(f"Sum of Digits = {sum+n}")
