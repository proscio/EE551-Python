# Patrick Roscio
# Lab_6 Queue.py
# Description: Defines three classes: Node, EmptyQueueException, and Queue to be used with mainQueue.py. 
#
# **Node Class**: The Node class defines the initial node structure containing the information "Data" to be stored in the node
#   as well as the adress of the next node innitialized to none. Accesors and Mutators are defined as well. 
#
# **EmpyQueueException Class** : This class defined the except statment used in mainQueue.py. It takes in a parameter for the action
#   trying to be preformed and outputs a message letting the user know that the action could not be completed within the Exception class
#   called as the superclass of this class. 
#
# **Queue Class**: This class includes all of the functions for the program beginning by initializing the head node to none. 
#    - The enQueue function takes in new data and assigns it as member of the Node class. Using the setNextNode mutator, we assign the new node to
#      the tail node. If the queue was empty, the tailnode also equals the head node.
#    - The deQueue function first checks to make sure the head node is not empty raising the exception if it is. The data in the headnode is assigned to
#       a returned variable "Data" and then the next node in the queue is assigned as the head node removing the data from the queue. 
#    - Peek make sure The head node is not empty and then returns the data in the head node. 
#    - Clear sets the head node to 'NONE' removing refrence to all of the other data in the node and allowing the garbage collector to delete it
#    - __str__() returns an empty string if the queue is empty and otherwise develops a list of data in the queue returned as a comma seperated string
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

class EmptyQueueException(Exception):
    def __init__(self, action):
        self.__message = f"The Queue was empty. {action} could not be performed."
        super().__init__(self.__message)

class Queue:
    def __init__(self):
        self.__headNode = None
        self.__tailNode = None
    def enQueue(self,data):
        new_node = Node(data)
        if self.__headNode is None:
            self.__headNode = new_node
            self.__tailNode = new_node
        else:
            self.__tailNode.setNextNode(new_node)
            self.__tailNode = new_node
    def deQueue(self):
        if self.is_empty():
            raise EmptyQueueException("De-queue")
        data = self.__headNode.getData()
        self.__headNode = self.__headNode.getNextNode()
        if self.__headNode is None:
            self.__tailNode = None
        return data
    def peek(self):
        if self.is_empty():
            raise EmptyQueueException("Peek")
        return self.__headNode.getData()
    def clear(self):
        self.__headNode = None
    def __str__(self):
         if self.is_empty():
             return ""
         index = self.__headNode
         queueData = []
         while index:
             queueData.append(str(index.getData()))
             index = index.getNextNode()
         return ','.join(queueData)
    
    # def __str__(self):
    #     print("Inside __str__ method")
    #     if self.is_empty():
    #         return ""
    #     index = self.__headNode
    #     queueData = []
    #     while index:
    #         queueData.append(str(index.getData()))
    #         index = index.getNextNode()
    #     result = ','.join(queueData)
    #     print("Queue data:", result)
    #     return result

    def is_empty(self):
        return self.__headNode is None
