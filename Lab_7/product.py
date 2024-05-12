#Patrick Roscio
#Lab_7 Product.py
#Description: Class deffinitions, getter, amd setter functions for class "Product". Also includes order summary print statment. 

class Product:
    def __init__(self):
        self.__name  = ""
        self.__num_units = 0
        self.__price_per_unit = 0
        self.__order_cost = 0
    
    def setName(self,name):
        self.__name = name
    def getNumUnits(self):
        return self.__num_units
    def setNumUnits(self,numUnits):
        self.__num_units = numUnits
    def getPPU(self):
        return self.__price_per_unit
    def setPPU(self,PPU):
        self.__price_per_unit = float(PPU)
    def setCost(self,total_cost):
        self.__order_cost = total_cost
    def __str__(self):
        return f"Order Summary:\n\tItem name: {self.__name}\n\tPrice per Unit: ${self.__price_per_unit: .2f}\n\tNumber of Units: {self.__num_units}\n Total: ${self.__order_cost: .2f}"

