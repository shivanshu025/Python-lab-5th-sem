""" Take Student full name and roll number. Generate email using first 3 letters of first name, first 3 letters of last name, and last 3 characters of roll number."""

fname = input("Enter first name : ")
lname = input("Enter last name : ")
roll =  input("Enter Roll No: ")
email = fname[:3] + lname[:3] + roll[-3:]
print("Generated Email:", email)
