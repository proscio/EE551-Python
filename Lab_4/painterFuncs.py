def intro():
    """Intro takes in user inputs such as the painitng selection and the Border charachter.
        The Function returns two variables: Selection and Border"""

    print("Welcome to the ASCII Painter")
    Selection = int(input("Please select an image \n 1-Sleeping Cat \n 2-Sailing Ship \n 3-cross \n 4-Old Timey Candle \n (Enter Choice as a number)"))
    Border = input("Please Select a charachter to use as a border!")
    print (f"You have selected {Selection} and {Border} as a border.")
    return Selection,  Border

def printHeaderFooter(Border, length):
    """Takes in the Border selection and the desired length as called by other functions. Returns the proper length border as a string: header_footer"""
    index = 0 
    header_footer = Border
    while index <= length:
        header_footer += Border
        index += 1
    return header_footer
    

def sleeping_cat(Border):
    """Prints a Sleeping cat! Intakes the variable "Border" as the Border Selection """
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
    """Prints a Sailing Ship! Intakes the variable "Border" as the Border Selection """

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
    """Prints a Blank Canvas! Intakes the variable "Border" as the Border Selection """
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
    """Prints a Cross! Intakes the variable "Border" as the Border Selection """
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
    """Prints an Old Timey Candle!! Intakes the variable "Border" as the Border Selection """
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
