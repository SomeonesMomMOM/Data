import json
from vending_machine import VendingMachine
from product import Product

def load_products(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data['products'], data['change']
    except FileNotFoundError:
        print("Error: products.json not found.")
        exit(1)
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        exit(1)

def save_products(file_path, products, change):
    with open(file_path, 'w') as file:
        json.dump({"products": products, "change": change}, file, indent=4)

def main():
    file_path = "products.json"
    products_data, initial_change = load_products(file_path)
    products = [Product(**product) for product in products_data]
    vending_machine = VendingMachine(products, initial_change)

    try:
        while True:
            vending_machine.display_products()
            money_inserted = float(input("Please insert money: "))
            product_id = int(input("What would you like to buy? "))
            vending_machine.process_purchase(product_id, money_inserted)
    except KeyboardInterrupt:
        print("\nBye!")
        save_products(file_path, [product.to_dict() for product in vending_machine.products], vending_machine.change)

if __name__ == "__main__":
    main()
