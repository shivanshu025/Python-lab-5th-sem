""" Wrtie a python program to fill the given letter template with name and date.
letter='''
Dear <Name>,
You are selected
<Date>
'''
"""

# name = input("Your Name: ")
# date = input("Enter date: ")
# print(f"Dear {name}, \nYou are selected!\n{date}")

# or

letter='''
Dear <Name>,
You are selected
<Date>
'''
name = input("Enter Name: ")
date = input("Enter date: ")

letter = letter.replace("<Name>", name)
letter = letter.replace("<Date>", date)
print(letter)