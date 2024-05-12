name = input("What is your name? ")
age = int(input ("How old are you? "))
if  age > 130:
    print (age, "is an invalid age. Please select a number below 130")
else:    
    print(name, "is", age, "years old!")
    exit()
