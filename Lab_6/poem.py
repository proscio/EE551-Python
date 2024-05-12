#Patrick Roscio
#Lab_6 poem.py
#  This file takes in the name of a file from a user, checks for the existance of that file, then devlopes a 
# short summary of that file consisting of the Author, Title, and number of lines as well as the first 3 lines. 

import os
poem = []

def main():
    i=0
    file_name = input("Please type the name of the file you would like to open: ")
    Presence = os.path.exists(file_name)
    while Presence == False:
        print("File not found!") 
        file_name = input("Please type the name of the file you would like to open: ")
        Presence = os.path.exists(file_name)
    if Presence == True:
        print("The file has been found!")
        poem_file = open(file_name, 'r')
    for line in poem_file:
        line.strip()
        poem.append(line)
        i += 1
    title = poem[0]
    author = poem[1]
    length = len(poem) - 2
    poem_content = poem [2:i]
    poem_summary = (f"Summary of: {title}By: {author}This poem has {length} lines! \n {poem_content[0]} {poem_content[1]} {poem_content[2]}")
    summary_file= open("lab_6/output.txt" ,"w")
    summary_file.write(poem_summary)
    poem_file.close
    summary_file.close



main()