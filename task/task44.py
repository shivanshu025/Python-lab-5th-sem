""" Take roll number like 2024A1R057 and extract admission year, program code,and roll number digits using slicing."""
roll = input("Enter roll number : ")
admission_year = roll[:4]
program_code = roll[4:6]
roll_number = roll[7:]
print("Admission Year:", admission_year)
print("Program Code:", program_code)
print("Roll Number:", roll_number)