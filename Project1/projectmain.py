#Patrick Roscio
#March 4th 2024
#EE 551 Engineering programming python: Project 1
#projectmain.py
#This is the main function and executable script of the program. This function handles the game parameters, output of instructions, and win/loss conditions


import projectFuncs

def main():
    game_parameters = {"s_bees" : 5, "w_bees": 5, "pollen" : 0, "score_to_win" : 20} #innitalization of game parameters
    
    flower_values = projectFuncs.value_loader()
    try:
        field = projectFuncs.create_field(flower_values)
    except TypeError as printme:
        print("Exception Raised: ", printme, TypeError)
        exit(-1)
    field_blank = projectFuncs.blank_field_creator(field)
    field_player = field_blank #initially sets the player field to the blank field from blank_field_creator
    projectFuncs.game_intro(flower_values, game_parameters)
    projectFuncs.field_printer(field_player)
    while (game_parameters["s_bees"] > 0 or game_parameters["w_bees"] > 0) and game_parameters["pollen"] < game_parameters["score_to_win"]:
        input_ok = False #boolean variable to check if bee type is equal to S or W
        print(f"You have {game_parameters['s_bees']} scout bees and {game_parameters['w_bees']} worker bees remaining!\n\tPollen Count: {game_parameters['pollen']}")
        while input_ok == False:
            bee_type_input = input("Select a bee W=worker, S=scout : ") #input of bee type
            bee_type_input = bee_type_input.upper() #converon to uppercase
            if bee_type_input == "W" or bee_type_input == "S":
                input_ok = True
            else:
                print("Invalid Bee Type! Please input again: ")
        y_coordinate = int(input("Please enter an X coordinate: ")) #Y-axis input(uptimately reversed in game mechanics but works )
        x_coordinate = int(input("Please enter a Y coordinate: ")) #x-axis input
        field_player, game_parameters = projectFuncs.game_mechanics(field, field_player, x_coordinate, y_coordinate, flower_values,game_parameters, bee_type_input)
        projectFuncs.field_printer(field_player)
    if game_parameters["pollen"] > game_parameters["score_to_win"]:
        print(f"You win!\nPollen Gathered for hive = {game_parameters['pollen']}")
    else: 
        print(f"You Lose :-( \nPollen Gathered for hive = {game_parameters['pollen']}\n")

main()
#end of main