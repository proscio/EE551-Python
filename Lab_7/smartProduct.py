#Patrick Roscio
#Lab_7 smartProduct.py
#Description: Class deffinitions, getter, amd setter functions for class "SmartProduct". Also includes order summary print statment. 

class SmartProduct:
    def __init__(self,ID,name,numUnits,price):
        self.__ID = ID
        self.__name  = name
        self.__num_units = numUnits
        self.__price_per_unit = price
        self.__order_cost = price*numUnits
    
    def getNumUnits(self):
        return self.__num_units
    def getPPU(self):
        return self.__price_per_unit
    def __str__(self):
        return f"--------------------\n\tItem name: {self.__name}\n\tPrice per Unit: ${self.__price_per_unit: .2f}\n\tNumber of Units: {self.__num_units}\n\tTotal cost of {self.__name}: ${self.__order_cost: .2f}"