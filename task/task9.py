""" Write a python program to take distance in kilometers and convert it into meters, centimeters, and millimeters. """

km = float(input("Enter the distance in km : "))
m = km*1000
cm = m*100
mm = cm*10

print("Distance in metre = ", m)
print("Distance in centimetre = ", cm)
print("Distance in millimetre = ", mm)
