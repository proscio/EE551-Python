# Patrick Roscio
# Lab_6 paintByNumbers.py
# Main Function of pbn lab. 

import pbnFunctions

def main():
    file_name = pbnFunctions.getFileName()
    pbnFunctions.processFile(file_name)
    print("Your image is located in the file painting.txt!")

main()