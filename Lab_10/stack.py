#Patrick Roscio
# Lab_ 10 stack.py
# Description: Defines three classes: Node, EmptyStackException, and Stack to be used with mainStack.py. 
#
# **Node Class**: The Node class defines the innitaal node structure containing the infromation "Data" to be stored in the node
#   as well as the adress of the next node innitialized to none. Accesors and Mutators are defined as well. 
#
# **EmpyStackException Class** : This class defined the except statment used in mainStack.py. It takes in a parameter for the action
#   trying to be preformed and outputs a message letting the user know that the action could not be completed within the Exception class
#   called as the superclass of this class. 
#
# **Stack Class**: This class includes all of the functions for the program beginning by initializing the head node to none. 
#    - The Push function  takes in new data and assigns it as member of the Node class. Using the setNextNode mutator, we assign the new node
#      as the headNode pushing the remaining nodes down the stack
#    - The pop node first checks to make sure the head node is not empty raising the exception if it is. The data in the headnode is assigned to
#       a returned variable "Data" and then the next node in the stack is assigned as the head node removing the data from the stack. 
#    - Peek make sure The head node is not empty and then returns the data in the head node. 
#    - Clear sets the head node to 'NONE' removing refrence to all of the other data in the node and allowing the garbage collector to delete it
#    - __str__() returns an empty string if the stack is empty and otherwise develops a list of data in the stack returned as a comma seperated string
#    - isEmpty() returns True if the head node is None and False if it contains data. 


class Node:

    def __init__(self, data):
        self.__data = data
        self.__nextNode = None
    def getData(self):
        return self.__data
    def getNextNode(self):
        return self.__nextNode
    def setData(self,data):
        self.__data = data
    def setNextNode(self,nextNode):
        self.__nextNode = nextNode
class EmptyStackException(Exception):
    def __init__(self, action):
        self.__message = f"The Stack was empty. {action} could not be performed."
        super().__init__(self.__message)

class Stack:
    def __init__(self):
        self.__headNode = None
    def push(self,data):
        new_node = Node(data)
        new_node.setNextNode(self.__headNode)
        self.__headNode = new_node
    def pop(self):
        if self.is_empty():
            raise EmptyStackException("Pop")
        data = self.__headNode.getData()
        self.__headNode = self.__headNode.getNextNode()
        return data
    def peek(self):
        if self.is_empty():
            raise EmptyStackException("Peek")
        return self.__headNode.getData()
    def clear(self):
        self.__headNode = None
    def __str__(self):
        if self.is_empty():
            return ""
        index = self.__headNode
        stackData = []
        while index:
            stackData.append(str(index.getData()))
            index = index.getNextNode()
        return ','.join(stackData)
    def is_empty(self):
        return self.__headNode is None

        

    
    
