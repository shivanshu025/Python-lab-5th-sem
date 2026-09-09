""" Write a python program to calculate the final bill amount after applying a discount. The program should take the total bill amount as input from the user and apply the discount according to the following rules. After calculating the discount, the program should display the discount amount and the final bill amount payable by the customer.
Bill Amount     Discount
Abouve 5000     20 Percent
3000 to 5000    10 Percent
Below 3000      No discount
"""
bill = int(input("Enter the Amount : "))
dis = 0
if(bill > 5000):
    dis = bill*0.2
elif(bill<=5000 and bill>=3000):
    dis = bill*0.1

print(f"Discount Amount : {dis} | Total Bill Amount : {bill-dis}" )
