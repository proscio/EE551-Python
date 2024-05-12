# Patrick Roscio
# January 29th, 2024
# Lab_2 lineSlope.py

x1 = float(input("Please enter the starting X coordinate: "))
y1 = float(input("Please enter the starting Y coordinate: "))
x2 = float(input("Please enter the ending X coordinate: "))
y2 = float(input("Please enter the ending Y coordinate: "))

Slope = (y1-y2)/(x1-x2)

print ("The Slope of the line is: ", format(Slope,'.3f'))