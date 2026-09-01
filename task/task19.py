""" Write a python program to take marks of htree subjects out of 100. Print True if the student scored atleast 40 in all three subjects and average marks are at least 50"""

a = int(input("Subject 1 : "))
b = int(input("Subject 2 : "))
c = int(input("Subject 3 : "))
avg = (a+b+c)/3
print(a>=40 and b>=40 and c>=40 and 50<= avg <= 100)