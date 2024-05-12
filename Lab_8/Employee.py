#Patrick Roscio
# Lab_8 Employee.py
#Description: class definition for employee.py and basic pay calculation. 

class Employee:
    def __init__(self, name, ID, pay):
        self.__name = name
        self.__ID = ID
        self.__pay = pay
    
    def calcPay(self, hours):
        return hours * self.__pay
  
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_ID(self):
        return self.__ID

    def set_ID(self, ID):
        self.__ID = ID

    def get_pay(self):
        return self.__pay

    def set_pay(self, pay):
        self.__pay = pay
