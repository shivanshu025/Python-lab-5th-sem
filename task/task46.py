""" Take name, branch, and year. Generate a code name using string concatenation, slicing and repetition."""
student_name = input("Enter student name : ")
branch_name = input("Enter branch: ")
year = input("Enter year : ")

code_name = student_name[:3] + "-" + branch_name[:3] + "-" + year[-2:]
print("Student Code",code_name)