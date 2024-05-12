# Patrick Roscio
# Lab_6 mainStack.py
# Description: From the stack.py file, imports classes "Stack" and "EmptyStackException" After reading in the input stack file, the 
# first string in the line is denoted as the opperation, for each possible opperation, a try/except statment is ran to call in the Stack 
# functions to Push, Peek, Pop, or Clear the stack. If the opperation cannot be ran, the exeption is called informing the user that the
# opperation could not be preformed

from stack import Stack, EmptyStackException

def main():
    stack = Stack()
    with open("Lab_10/inputStack.txt", "r") as file:
        for line in file:
            operation = line.strip().split()
            if operation:
                command = operation[0]
                if command == "push":
                    value = operation[1]
                    try:
                        stack.push(value)
                        print(f"Pushed: {value}")
                    except EmptyStackException as e:
                        print(e)
                elif command == "pop":
                    try:
                        value = stack.pop()
                        print(f"Popped: {value}")
                    except EmptyStackException as e:
                        print(e)
                elif command == "peek":
                    try:
                        value = stack.peek()
                        print(f"Peek: {value}")
                    except EmptyStackException as e:
                        print(e)
                elif command == "clear":
                    stack.clear()
                    print("Stack cleared.")
                else:
                    print(f"All values in the Stack: {stack}")

main()