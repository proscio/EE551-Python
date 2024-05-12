#Patrick Roscio
#Lab_6 averages.py
#After checking for the file's existence, this program reads in lines from a .txt file and sums all 
# their values. Adter which, it divides the sum by the number of values in the file returning the average.  

import os
existance = os.path.exists("Lab_6\\numbers.txt")
print(f"File test returned: {existance}")

def main():
    sum = 0
    divider = 0
    source_file = open("Lab_6\\numbers.txt" ,"r")
    for line in source_file:
        line.strip()
        line = int(line)
        print(line)    
        sum += line
        divider += 1 
    Average = sum/divider
    source_file.close()
    print("The average value was: ", format(Average, '.2f'))

main()