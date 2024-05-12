#Patrick Roscio
#Lab_7 smartOrderSystem.py
# Description: User inputs, product definition as object of class "smartProduct" and total cost calculation. 

from smartProduct import SmartProduct

def calcTotal(productList):
    total_cost = 0
    for i in productList:
        price_per_unit = SmartProduct.getPPU(i)
        num_Units = SmartProduct.getNumUnits(i)
        item_cost = float(price_per_unit) * float(num_Units)
        total_cost += item_cost
    return total_cost

def main():
    i = 1
    productList = []
    num_additions = int(input("Please enter the number of items you would like to order: "))
    for i in range(1, num_additions + 1):
        Unique_id = str(i) + "squ" 
        Item_added = str(input(f"Please enter the name of item {i}:"))
        price_per_item = 9.99
        num_items = int(input(f"Please enter the number of {Item_added}s you would like to order: "))
        product = SmartProduct(Unique_id,Item_added, num_items, price_per_item)
        productList.append(product)
        i += 1
    total_cost = calcTotal(productList)
    print("\nOrder Summary:")
    for product in productList:
        print(product)
    print("--------------------")
    print(f"Your order total is: ${total_cost: .2f}\n")

main()