#Patrick Roscio
#Lab_7 order_system.py
# Description: User inputs, product definition as object of class "Product" and total cost calculation. 

from product import Product

def calcTotal(product):
    price_per_unit = Product.getPPU(product)
    num_Units = Product.getNumUnits(product)
    total_cost = float(price_per_unit) * float(num_Units)
    return total_cost

def main():
    product = Product()
    name = input("Please enter the name of the product: ")
    Product.setName(product,name)
    numUnits = input("Please enter the number of units: ")
    Product.setNumUnits(product,numUnits)
    Product.setPPU(product,9.99)
    total_cost = calcTotal(product)
    Product.setCost(product,total_cost)
    print(product)

main()