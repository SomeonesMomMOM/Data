import json
from product import Product
import os


class VendingMachine:

    def __init__(self, change, products):
        self.change = change
        self.products = products #product class is being passed here

        
    def find_product(self, choice):

        for product in self.products:
            if product.number == choice:
                return product
             
        print('Invalid choice! Choose one of the given product numbers!')
    
    def check_money(self, product, cash):
        if cash < product.price:
            print(f'You cannot afford the {product.name}, Price: {product.price}€')
        
        if cash >= product.price:
            if product.stock <= 0:
                print('Sorry, product slot empty!')

            else:
                newchange = self.change - (cash - product.price)
                if newchange < 0:
                    print('Sorry, no change left inside the vending machine! No purchase is being made, Loser!')
                else:
                    print(f'Thanks for the purchase, product is being served!')
                
                    product.stock -= 1
            
                    self.change = newchange
        
        return product.stock, self.change
    
    def save_vending_machine(self, products, filename):
        """Save vending machine change and products to a JSON file."""

        products = [{"name": product.name,
                    "price": product.price,
                    "stock": product.stock,
                    "number": product.number}
                    for product in self.products]
        
        data = {"change": self.change, "products": products}

        with open(f"/Users/Jakob/p4p/vendingmachine/src/json_files/{filename}", 'w') as file:
            json.dump(data, file)

    


                

