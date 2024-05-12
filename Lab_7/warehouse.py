#Patrick Roscio
#Lab_7 warehouse.py
#Description: Class deffinition of warehouse

class Warehouse:
    def __init__ (self,totalGoods):
        self.__totalGoods = totalGoods
    
    def addGoods(self):
        numAdd = int(input("Please enter the number of goods to add: "))
        self.__totalGoods += numAdd
    def remGoods(self):
        i = 1
        numRem = int(input("Please enter the number of goods to remove: "))
        while i == 1:
            if numRem <= self.__totalGoods:
                self.__totalGoods -= numRem
                i = 0
            else:
                print("Not enough goods remaining!")
                numRem = int(input("Please enter the number of goods to remove: "))
    def __str__(self):
        return f"Total Number of goods in Warehouse: {self.__totalGoods}."

        