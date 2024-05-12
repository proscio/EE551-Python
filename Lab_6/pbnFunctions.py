#Patrick Roscio
#Lab_6 pbnFunctions.py

import os

def getFileName():
    """Prompts User for a file path and returns the file (read only) in a variable if present. """    
    file_name = input("Please type the name of the file you would like to open: ")
    Presence = os.path.exists(file_name)
    while Presence == False:
        print("File not found!") 
        file_name = input("Please type the name of the file you would like to open: ")
        Presence = os.path.exists(file_name)
    if Presence == True:
        print("The file has been found!")
    return (file_name)

def convertLine(line):
    """With input line as a comma seperated set of numbers, returns a new line as charachters."""
    line = line.strip()
    new_line = ""
    for x in line.split(','):
        if x == "1":
            new_line += " "
        elif x == "2":
            new_line += ","
        elif x == "3":
            new_line += "_"
        elif x == "4":
            new_line += "("
        elif x == "5":
            new_line += "O"
        elif x == "6":
            new_line += ")"
        elif x == "7":
            new_line += "-"
        elif x == "8":
            new_line += "\""
    return(new_line)
    
def processFile(file_name):
    """Opens the file in file path \"file_name\" and iterates
     through the lines of the file to create a new image file"""
    raw_image = open(file_name, "r")
    output_file = open("Lab_6/painting.txt", "w")
    for line in raw_image:
        new_line = convertLine(line)
        output_file.write(new_line + "\n")
    raw_image.close()
    output_file.close()


    
    
