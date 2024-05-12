import painterFuncs
def main():
    Selection, Border = painterFuncs.intro()
    if Selection == 1:
        painterFuncs.sleeping_cat(Border)    
    elif Selection == 2:
        painterFuncs.sailing_ship(Border)
    elif Selection == 3:
        painterFuncs.cross(Border)
    elif Selection == 4:
        painterFuncs.candle(Border)
    else:
        painterFuncs.blank(Border)
        exit(-1)

main()