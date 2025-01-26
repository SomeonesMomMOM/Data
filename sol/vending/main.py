import os
import json

from product import Product
from vending_machine import VendingMachine

def load_vending_machine(filename):

    if not os.path.exists(filename):
        print("file products.json not found. Initializing new vending machine.")
        return None, None
    
    

    with open(filename, "r") as file:
        data = json.load(file) 
    
    change = data["change"]

    products = [
            Product(p["name"], p["price"], p["stock"], p["number"])
            for p in data["products"]
        ]

    return change, products
    

def main():

    while True:
    
        filename = "products.json"

        change, products = load_vending_machine(filename)

        if change is not None and products is not None:
            
            pass

        else:    
            change = 10.00
            product1 = Product(name="Coke", price=1, stock=4, number=1)
            product2 = Product(name="Pepsi", price=2, stock=5, number=2)
            products = [product1, product2]
            
        vm = VendingMachine(change, products)

        print(f'Change: {vm.change}')
        print("Vending machine products:")

        for product in vm.products:
                print(str(product)) 
                    
        while True:

            choice = int(input('Choose a product (to exit press Ctrl + C):').strip())
            cash = float(input('Enter money (float):'))
            
            if type(choice) and type(cash) is float:
                serveproduct = vm.find_product(choice)
                vm.check_money(serveproduct, cash)
                break
            else:
                print('Input is not an integer, try again!')


        vm.save_vending_machine(vm.products, filename)


        # Run the main function
if __name__ == "__main__":

    main()