#Patrick Roscio
#Lab_5: labManager.py
#This program presents a menu of options for the user. If the usser selects option 1 to add equipment, the list "Assets" is appended adding the
# new equipment to the end of the list up to 5 items. The user can then view the list, remove items from the list, or exit the program. 
assets = []
def current_inventory():
    """Prints current inventory"""
    print ("Current Inventory:") 
    for i in assets:
            print ("\t" ,i)
def main():    
    run = "Yes"
    print("Welocome to the Lab Manager")
    while run == "Yes":
        selection = int(input("Please Select and Option: \n \t 1. Add Equipment \n \t 2. Remove Equipment \n \t 3. Display Current Equipment\n \t 4. Leave the Lab manager \n"))
        if selection == 1: 
            quantity = len(assets)
            if quantity <= 4:
                assets.append(input("Please enter the name of the equipment you wish to add: "))
            else:
                print("The lab is full. No more equipment can be added at this time.")
        elif selection == 2:
            current_inventory()
            remove_equipment = input("Ener the name of the Equipment you wish to remove: ")

            for i in range(len(assets)):
                if assets[i] != remove_equipment:
                    print("This eqipment is not present in slot: ", i)
                else:
                    assets.remove(remove_equipment)
                    print(f"Equipment {remove_equipment} removed.")
                    break
        elif selection == 3:
            current_inventory()
        else:
            exit()

main()