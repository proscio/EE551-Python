#Patrick Roscio
#March 4th 2024
#EE 551 Engineering programming python: Project 1
#projectfuncs.py
#This file contains all necessary functions for projectmain.py. Please see each function's docstring for a description. 

import os

def value_loader():
    """Imports the .csv file from the user containing the point values for the game.
        Returns a dictionary \"flower_value_file\" containing tuples with the flower 
        identifier, name, and assosiated point value. """
    
    flower_values = {} #Innitialization of dictionary that will contain flower values


    #File Detection While loop: 
    flower_value_file_name = input("Please enter the file name containing flower types: ")
    presence = os.path.exists(flower_value_file_name)
    while presence == False:
        print("File Not Found!")
        flower_value_file_name = input("Please enter the file name containing flower types: ")
        presence = os.path.exists(flower_value_file_name)
    

    #Flower_values Dictionary creation    
    flower_value_file = open(flower_value_file_name,"r")
    for line in  flower_value_file:
        line.strip()
        value = line.split(",")
        flower_values[value[0]] = (value[0],value[1],value[2][0:1])
    flower_value_file.close()


    return(flower_values)



          
def create_field(flower_values):
    """Prompts the user for the location of the field file. Checks to make sure flowers from 
        the field file are present in the points file (See: value_loader) and raises an 
        error if not. Returns the two dimensional list \"field\" ."""
    field = [] #initiaization of hidden field
    acceptable_flower_values = ["H","P"," "] #innitialization of the acceptable list containing values found in the flowerlist files.
                                             #This also includes "H" for the hive, "P" for pincher plants, and " " for blank spaces.
    
    #File Detection While loop: 
    field_file_name = input("Please enter the file name containing field! : ")
    presence = os.path.exists(field_file_name)
    while presence == False:
        print("File Not Found!")
        field_file_name = input("Please enter the file name containing field! : ")
        presence = os.path.exists(field_file_name)

    #This section build the hidden field from the imported csv file. 
    field_file = open(field_file_name, "r")
    for key in flower_values:
        acceptable_flower_values.append(key) #copies values from the flower list into acceptable list
    for line in field_file:
        row =  line.strip().split(",")
        for i in range(len(row)): #Small repair to fix read-in issue
            if row[i] == '':
                row[i] = ' '  
        
        #This for loop makes sure that all value sin the fiels are also in the accetable list. Returns an error if not
        for i in row:
            if i not in acceptable_flower_values and i != "":
                print(f"Bad Value: {i}")
                raise TypeError("Flowers present on field with no assosicated decleration in Flower Value File!")
        field.append(row)
    return(field)



def blank_field_creator(field):
    """Using the dimensions of the imported field, (See: create_field) outputs a blank field of the same dimensions 
        retaining the position of the hive (Denoted: \"H\")"""
    field_blank = [["" for i in row]for row in field] #Innitializes the blank field to retain the dimenstions of the hidden field. Reffered to as field_player in main. 
    
    #For loop to retain the location of hive in the fied-blank 2d list.
    for r in range(len(field)):
        for c in range(len(field[r])):
            if field[r][c] == "H":
                field_blank[r][c] = "H"
    
    return(field_blank)



def field_printer(field):
    """Takes in the field list to be printed and outputs a graphic of the desired field. """
           
    header = [] #empty list containing row and column header eventually
    index_a = 0 #random index variable
    row_print = "" #innitializes what will eventually be added to each row as a column header. 
    header_print = "" #innitializes what will eventually be added to the top of the field as a header. 
    len_field_row = len(field[0]) #length of the x-axis
    len_header = len(header) #length of the y axis
   
    #Building Innitial header
    while len_field_row >= len_header + 1:
        added_value = str(index_a)
        header.append(added_value)
        index_a += 1
        len_header = len(header)

    #printing innitial header with formatting for spacing
    print("\n", end="")
    header_print = ""
    for i in range(len(header)):
        header_print += " " + str(header[i]) + "  "
    print(f"    {header_print}")

    #Printing field with column header values and "|" as columns
    for r in range(len(field)):
        row_print = ""
        for c in range(len(field[r])):
            if len(field[r][c]) < 1:
                field[r][c] += " "
            row_print += (f"| {field[r][c]} ")
        print(f"{header[r]}  {row_print}|")

print("\n")



def game_intro(flower_values,game_paremeters):
    """Prints the game instructions as well as relevant information such as number of bees, flower values, and points needed to win. 
        takes in flower_values (See: Value_Loader) and game_parameters (See: Main) Input: (Flower_values, Game_parameters)"""
    
    print(f"Welcome to Bee line!")
    print("Instructions:\n\tYour goal is to colect as much Pollen for your hive as possible playing as the Queen bee!")
    print(f"\tAs the Queen, you can disptach both types of bees in your hive: ")
    print(f"\tScout bees: Qty:{game_paremeters['s_bees']} | Scout bees check a location for polen returning a 3x3 grid of flowers around them.")
    print(f"\tWorker Bees: Qty:{game_paremeters['w_bees']} | Workers bees are sent to a location, reveal the flowers in a 3x3 grid centered on that location, and harvest polled from any unharvested flowers\n""")
    print(f"\tWarning! Pitcher plants will trap your bee, regardless of the type. make sure your bees stay away!")
    print(f"\tYou will be able to make a selecetion for the type of bee (W or S) and the x and y location on the grid!")
    print(f"\tPlease Note: each bee can only leave the hive once and each flower can only be harvested once!")
    print(f"\nDifferent flowers have Different Point Values!")
    print(f" \nName of Flower:   | Identifier: | Point Value:")
    
    #Prints flower list a table:
    for i in flower_values:
        flower_string =(flower_values[i])       
        print(f" {flower_string[1]:<16} | {flower_string[0]:<11} | {flower_string[2]}")
    
    return()



def game_mechanics(field_hidden, field_player, x_coordinate, y_coordinate, flower_values,game_parameters, bee_type_input): 
    """Takes in several parameters including the set game parameteres, X and Y coordinates from the user, flower values to keep track
        of the score, as well as both hidden and visible fields. The function derecates the appropriate values when a bee is used as
        well as keeps track of the bounds of th field to alert if the bee has flown away. The function checks if the 3x3 area a bee has 
        been sent t contains a pincher plant and returs the appropriate message if so. If there is no pincher, the values form the hidden
        field are coppied into the visible field and output to the user. If bee type is a worker, the corrct amount of pollen is harvested,
        hidden field isstripped of it's values in that area, and the flower in the visible field are turned to U for used. 
        Returns(field_player, game_parameters) to main() """
    
    y_bound = len(field_hidden[0]) - 1 #innitializes field boundary in the x-axis
    x_bound = len(field_hidden) - 1 #innitializes field boundary in the y-axis
    flower_value_keys = list(flower_values.keys()) #Creates a list of all of the flower value keys within the dictioary of flower values

    #If loops to decrement the amount of bees from the game_parameters dictionatry. Aslo allerts the player of the type of bee being played as well as the condition of no remaining bees. 
    if bee_type_input == "S" and game_parameters['s_bees'] > 0:
        print("Sending out a Scout!")
        game_parameters['s_bees'] -= 1
    elif bee_type_input =='S' and game_parameters['s_bees'] == 0:
        print("No more Scout bees available!")
        return(field_player, game_parameters) #return to exit the function if the player tries to use a bee with none remaining.
    if bee_type_input == "W" and game_parameters['w_bees'] > 0:
        print("Sending out a Worker!")
        game_parameters['w_bees'] -= 1
    elif bee_type_input == 'W' and game_parameters['w_bees'] == 0:
        print("No more Worker bees available!")
        return(field_player, game_parameters)


    #Boundary test for field
    if x_coordinate > x_bound:
        print("Oh No! Your bee has flown too far away from the hive and has been lost!")
    elif y_coordinate > y_bound:
        print("Oh No! Your bee has flown too far away from the hive and has been lost!")
    else:
        examine_area = [] #one dimensional list containing all of the vairables in the search area. Used to check for the presence of a pincher plant "P"
       
        #for loop to creade the 3x3 area dimentions or smaller area depending the bee is placed on a boundary line of the field       
        for r in range(max(0, x_coordinate - 1), min(x_coordinate + 2, len(field_hidden))):
            for c in range(max(0, y_coordinate - 1), min(y_coordinate + 2, len(field_hidden[0]))):
                row_index = max(0, min(r, x_bound))
                col_index = max(0, min(c, y_bound))
                examine_area.append(field_hidden[row_index][col_index])
        
        #If loop to check for presence of pincher plant or run the main function of copying over necesary list values to field_player. 
        if "P" in examine_area:
            print("Oh no! Your bee did not return! It must have been eaten by a Pitcher plant!")
        else:
            for r in range(max(0, x_coordinate - 1), min(x_coordinate + 2, len(field_hidden))):
                for c in range(max(0, y_coordinate - 1), min(y_coordinate + 2, len(field_hidden[0]))):
                    row_index = max(0, min(r, x_bound))
                    col_index = max(0, min(c, y_bound))
                    
                    #If loop to check bee type and copy over flower variables if preseent in field_hidden. Also if bee_type_input is "W", turns values to "U" for used and increases pollen score. 
                    if bee_type_input == "S" and field_player[row_index][col_index] != "U":
                        field_player[row_index][col_index] = field_hidden[row_index][col_index]
                    elif bee_type_input == "W" and field_hidden[row_index][col_index] != " ":
                        field_player[row_index][col_index] = "U"
                        if field_hidden[row_index][col_index] in flower_value_keys:
                            game_parameters['pollen'] += int(flower_values[field_hidden[row_index][col_index]][2])
                            field_hidden[row_index][col_index] = " "

    return(field_player, game_parameters)

#end of functions