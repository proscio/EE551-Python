# Patrick Roscio
# Lab 9 Powers.py
# Description: Exploring Recurion, This script takes in two variables, Base_value and exponent. Calling a recursive function, it multiplies 
# the base value against the previous result until the exponent reaches 1, then returns the result in main. 

def powers(base_value, exponent_value):
    print (f"Powers({base_value},{exponent_value})")
    if exponent_value == 1:
        return base_value
    else: 
        exponent_value -= 1
        return base_value * powers(base_value, exponent_value)
    
def main():
    base_value = int(input("Please enter the base value: "))
    exponent_value = int(input("Please enter the exponent variable: "))
    final_value = powers(base_value, exponent_value)
    print(f"The Answer to {base_value}^{exponent_value} is: {final_value}")

main()