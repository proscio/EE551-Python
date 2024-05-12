#Patrick Roscio
# Lab_8 worker.py
#Description: class deffinition for the worker employee type. Subset of employee with added private variable: shift type. 

from Employee import Employee

class Worker(Employee):
    def __init__(self,name,ID,pay,shift):
        super().__init__(name,ID,pay)
        self.__shift = shift

    def getShift(self):
        if self.__shift == 1:
            return "Day Shift"
        else: 
            return "Night Shift"
            
    
    def setShift(self,shift):
        self.__shift = shift
    


