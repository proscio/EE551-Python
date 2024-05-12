#Patrick Roscio
#Lab_7 manager.py
#Description:main function of warehouse.py

from warehouse import Warehouse

def main():
    i = 1
    myWarehouse = Warehouse(0)
    while i == 1:
        print("Warehouse Options:\n\t1. Add Goods\n\t2. Remove goods\n\t3. Output Total\n\t4. Quit")
        option = int(input("Please select an option: "))
        if option == 1:
            Warehouse.addGoods(myWarehouse)
        elif option == 2:
            Warehouse.remGoods(myWarehouse)
        elif option == 3:
            print(myWarehouse)
        elif option == 4: 
            exit(0)
        else: 
            print("Invald Input!")

main()