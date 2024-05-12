# Patrick Roscio
# Lab_9 parenthesis.py
# Description: Using the user's input, main() calls a function parenTest which takes in an initial position, 0
#   and determines if length of the line is equal to position. If not, the count varable is incremented by 1 
#   for every ( and decremented by 1 for every ) recursively until the maximum position us reached. If so, the
#   function rreturns true if count == 0. 

count = 0

def parenTest(line, position):
    global count  
    if position == len(line):
        return count == 0
    if line[position] == '(':
        count += 1
    elif line[position] == ')':
        count -= 1
    if count < 0:
        return False
    return parenTest(line, position + 1)

def main():
    user_input = input("Enter a series of ( and ): ")
    result = parenTest(user_input, 0)
    if result:
        print("Parentheses are balanced.")
    else:
        print("Parentheses are not balanced.")


main()
