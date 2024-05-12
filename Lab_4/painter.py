#Patrick Roscio
#February 12, 2024
#Painter (1) lab Assignment

def intro():
    print("Welcome to the ASCII Painter")
    Selection = int(input("Please select an image \n 1-Sleeping Cat \n 2-Sailing Ship \n 3-cross \n 4-Old Timey Candle \n (Enter Choice as a number)"))
    Border = input("Please Select a charachter to use as a border!")
    print (f"You have selected {Selection} and {Border} as a border.")
    return Selection,  Border

def printHeaderFooter(Border, length):
    index = 0 
    header_footer = Border
    while index <= length:
        header_footer += Border
        index += 1
    return header_footer
    

def sleeping_cat(Border):
    L1 =  "       |\\\\      _,,,---,,_      "
    L2 =  " ZZZzz /,`.-'`'    -.  ;-;;,_   "
    L3 =  "      |,4-  ) )-,_. ,\\\\ (  `'-' "
    L4 =  "      '---''(_/--'  `-'\\\\_)     "
    longest_line = max(L1,L2,L3,L4)
    length = len(longest_line)+2
    header_footer = printHeaderFooter(Border,length)
    print("",header_footer,"\n",
        Border,L1,Border,"\n",
        Border,L2,Border,"\n",
        Border,L3,Border,"\n",
        Border,L4,Border,"\n",
        header_footer)
    
def sailing_ship(Border):
    L1 =  "      |    |    |            "
    L2 =  "     )_)  )_)  )_)           "
    L3 =  "    )___))___))___)\\\        "
    L4 =  "   )____)____)_____)\\\\\\\     "
    L5 =  " _____|____|____|____\\\\\\\\\\\__"
    L6 =  " \\\    Satisfaction   /      "
    L7 =  "^^^^^^^^^^^^^^^^^^^^^^^^^^^^ "
    longest_line = max(L1,L2,L3,L4,L5,L6,L7)
    length = len(longest_line)+2
    header_footer = printHeaderFooter(Border,length)
    print("",header_footer,"\n",
        Border,L1,Border,"\n",
        Border,L2,Border,"\n",
        Border,L3,Border,"\n",
        Border,L4,Border,"\n",
        Border,L5,Border,"\n",
        Border,L6,Border,"\n",
        Border,L7,Border,"\n",
        header_footer)

def blank(Border):
    L1 = "                  "
    L2 = "      BLANK       "
    L3 = "     CANVAS!      "
    L4 = "                  "
    L5 = "                  "
    longest_line = max(L1,L2,L3,L4,L5)
    length = len(longest_line)+2
    header_footer = printHeaderFooter(Border,length)
    print("",header_footer,"\n",
        Border,L1,Border,"\n",
        Border,L2,Border,"\n",
        Border,L3,Border,"\n",
        Border,L4,Border,"\n",
        Border,L5,Border,"\n",
        header_footer)
    
def cross(Border):
    L1 = "     .-.      "
    L2 = "   __| |__    "  
    L3 = "  [__   __]   "
    L4 = "     | |      "
    L5 = "     | |      "
    L6 = " jgs | |      "
    L7 = "     '-'      "
    longest_line = max(L1,L2,L3,L4,L5,L6,L7)
    length = len(longest_line)+2
    header_footer = printHeaderFooter(Border,length)
    print("",header_footer,"\n",
        Border,L1,Border,"\n",
        Border,L2,Border,"\n",
        Border,L3,Border,"\n",
        Border,L4,Border,"\n",
        Border,L5,Border,"\n",
        Border,L6,Border,"\n",
        Border,L7,Border,"\n",
        header_footer)
    
def candle(Border):
    L1 = "    )       "
    L2 = "   (_)      "
    L3 = "   |`|      "
    L4 = "   | |  _() "
    L5 = " \_|_|_/    "
    longest_line = max(L1,L2,L3,L4,L5)
    length = len(longest_line)+2
    header_footer = printHeaderFooter(Border,length)
    print("",header_footer,"\n",
        Border,L1,Border,"\n",
        Border,L2,Border,"\n",
        Border,L3,Border,"\n",
        Border,L4,Border,"\n",
        Border,L5,Border,"\n",
        header_footer)

def main():    
    Selection, Border = intro()
    if Selection == 1:
        sleeping_cat(Border)    
    elif Selection == 2:
        sailing_ship(Border)
    elif Selection == 3:
        cross(Border)
    elif Selection == 4:
        candle(Border)
    else:
        blank(Border)
        exit(-1)

main()