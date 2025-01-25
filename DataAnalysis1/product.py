class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def is_available(self):
        return self.stock > 0

    def purchase(self):
        if self.stock > 0:
            self.stock -= 1

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }

    def __str__(self):
        return f"{self.name}: {self.price} Euro ({'Out of stock' if self.stock == 0 else f'{self.stock} available'})"
