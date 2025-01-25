class VendingMachine:
    def __init__(self, products, initial_change):
        self.products = products
        self.change = initial_change

    def display_products(self):
        print("\nVending machine products\n" + "-" * 40)
        for i, product in enumerate(self.products, start=1):
            print(f"[{i}] {product}")
        print("-" * 40)

    def process_purchase(self, product_id, money_inserted):
        if not (1 <= product_id <= len(self.products)):
            print("Invalid product ID.")
            return

        product = self.products[product_id - 1]
        if not product.is_available():
            print(f"The product {product.name} is out of stock.")
            return

        if money_inserted < product.price:
            print(f"The price of {product.name} is {product.price} Euro, but you have only given {money_inserted} Euro.")
            return

        change_due = money_inserted - product.price
        if change_due > self.change:
            print(f"Sorry, I don’t have enough change for {money_inserted} Euro.")
            return

        product.purchase()
        self.change += product.price
        self.change -= change_due
        print(f"One {product.name}, there you go! Your change is {change_due:.2f} Euro.")
