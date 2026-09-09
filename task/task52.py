""" Write a program to input 5 students"""
for i in range(5):
    marks = int(input("Enter Marks: "))
    if marks <0 or marks>100:
        print("Invalid Marks skipped !")
    else:
        print("Marks are Valid")