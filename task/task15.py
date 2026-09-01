""" Wrtie a python program to take two inputs a and b, swap their values using a temporary variable, and print updated values."""

a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
print(f"a = {a}, b = {b}")
temp = a
a = b
b = temp
print(f"a = {a}, b = {b}")