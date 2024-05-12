#Patrick Roscio
#February 12, 2024
#Pyramid Area lab Assignment

import math 

a = float(input("Side length: "))
h = float(input("Pyramid height: "))

def calcTotalArea(a,h):
    square = math.sqrt(((a**2)/4)+h**2)
    total_area = a**2 + 2*a*square
    return total_area

def calcBaseArea(a):
    base_area = a*a
    return base_area

total_area = calcTotalArea(a,h)
base_area = calcBaseArea(a)
side_area = total_area - base_area


print(f"The base of the pyramid has an area of {base_area}ft.")
print(f"Each Side of the pyramid has an area of {side_area}ft.")
print(f"The total area of the Pyramid is {total_area}ft.")