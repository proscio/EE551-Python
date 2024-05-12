# Patrick Roscio
# February 6th, 2024
# Lab_3 uncertainty.py

import random

x_poss = random.randint(1,10)
y_poss = random.randint(1,10)

print("-------------------------------------------------------------------------------------------------------------------")
print("Welome to the random possition guesser! \nEach position variable (x,y) has a a range of 1 through 10! \nGood Luck!" )

i = int(input("How manu guesses yould you like? "))
while i>0:
    x_guess = int(input("Please enter a guess for X"))
    y_guess = int(input("Please enter a guess for Y"))
    if x_guess == x_poss and y_guess == y_poss:
        print("You win! The postion was (",  x_poss, ",", y_poss, ") !")
        exit()
    elif x_guess == x_poss and y_guess != y_poss:
        print("Your X Variable, ", x_guess, " is correct!")
        print("Please enter a new guess for y")
        i -= 1
    elif x_guess != x_poss and y_guess == y_poss:
        print("Your Y Variable, ", y_guess, " is correct!")
        print("Please enter a new guess for X")
        i -= 1
    else: 
        print("Incorrect! Please guess again!")
        i -=1
else: 
    print("Oh No! You are out of guesses, Better luck next time. ")
    print("The postion was (",  x_poss, ",", y_poss, ") !")


    
    