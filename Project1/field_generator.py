#Patrick Roscio
#March 4th 2024
#EE 551 Engineering Programming Python: Project 1
#field_generator.py
# Generates a random field based on input parameters and saves it to the .csv file provided. 

import os
import random

file_name = input("please enter the name and location of the file (.csv) to store the randomly-generated field: ")
file_checker = os.path.exists(file_name)
while file_checker == False:
    print("File not Found! ") 
    file_name = input("please enter the name of the file (.csv) to store the randomly-generated field: ")
    file_checker = os.path.exists(file_name)
x_dimension = int(input("Please input a dimention for the x-axis: "))
y_dimension = int(input("Please input a dimention for the y-axis: "))
pincher_plants = int(input("Please enter the number of pitcher plants you would like: "))
flower_file_name = input("Please enter the name of the flowerlist file you would like to use: ")
file_checker2 = os.path.exists(flower_file_name)
while file_checker2 == False:
    print("File not Found! ") 
    flower_file_name = input("please enter the name of the file (.csv) to store the randomly-generated field: ")
    file_checker2 = os.path.exists(flower_file_name)
flowers_desired = int(input("Please enter the number of flowers you would like on the field: "))
while ((x_dimension * y_dimension)-1) < (pincher_plants + flowers_desired):
    print("There are more flowers than spaces in the field!")
    flowers_desired = int(input("Please enter a lower number of flowers you would like on the field: "))

flower_types = []
flower_file = open(flower_file_name, 'r')
for line in  flower_file:
    line.strip()
    value = line.split(",")
    flower_types.append(value[0])
flower_file.close()

field = [[" " for i in range(x_dimension)] for c in range(y_dimension)]
x_hive = random.randint(0,x_dimension-1)
y_hive = random.randint(0,y_dimension-1)

field[y_hive][x_hive] = "H"

num_pincher = 0
num_flowers = 0
while num_pincher < pincher_plants:
    x_random = random.randint(0,x_dimension-1)
    y_random = random.randint(0,y_dimension-1)    
    if field[y_random][x_random] == ' ':
        field[y_random][x_random] = "P"
        num_pincher += 1

while num_flowers < flowers_desired:
    x_random = random.randint(0,x_dimension-1)
    y_random = random.randint(0,y_dimension-1)
    if field[y_random][x_random] == ' ':
        field[y_random][x_random] = random.choice(flower_types)
        num_flowers += 1

for row in field:
    print(row)

csv_file = open(file_name, 'w')
for row in field:
    csv_file.write(','.join(row)+ '\n')        
csv_file.close()

print("Field saved to", file_name)
