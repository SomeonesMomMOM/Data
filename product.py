import json
import os

class Product:
    def __init__(self, name, price, stock, number):
        self.name = name
        self.price = price
        self.stock = stock
        self.number = number  # ✅ Add number attribute

    def __str__(self):
        return f"Product {self.number}: {self.name}, Price: {self.price} €, Stock: {self.stock} available"
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Product name must be a string")
        else:
            self.__name = value

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Price must be a positive number")
        self.__price = value
    
    
       