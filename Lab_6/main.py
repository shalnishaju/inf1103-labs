import json
import os

from product import Product
from inventory import Inventory


# Create an Inventory object
inventory = Inventory()


# Load inventory from JSON file
def load_inventory():
    if not os.path.exists("inventory.json"):
        # Create initial products if no JSON file exists
        product1 = Product("P001", "Laptop", 1200.00, 15)
        product2 = Product("P002", "Mouse", 25.50, 40)
        product3 = Product("P003", "Keyboard", 45.00, 25)

        inventory.add_product(product1)
        inventory.add_product(product2)
        inventory.add_product(product3)

        return

    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)

        for item in data:
            product = Product(
                item["id"],
                item["name"],
                item["price"],
                item["stock"]
            )

            inventory.add_product(product)

        print("Inventory loaded successfully!")

    except (json.JSONDecodeError, KeyError, TypeError):
        print("Error loading inventory. Starting with an empty inventory.")


# Save inventory to JSON file
def save_inventory():
    products = []

    for product in inventory.get_all_products():
        products.append({
            "id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "stock": product.get_stock()
        })

    with open("inventory.json", "w") as file:
        json.dump(products, file, indent=4)

    print("Inventory saved successfully!")

# Display menu
def display_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


# Add product
def add_product():
    print("\nAdd New Product")

    product_id = input("Product ID: ").strip()

    if not product_id:
        print("Product ID cannot be empty.")
        return

    if inventory.search_product(product_id) is not None:
        print("Product ID already exists.")
        return

    product_name = input("Product Name: ").strip()

    if not product_name:
        print("Product name cannot be empty.")
        return

    while True:
        try:
            price = float(input("Price: "))

            if price < 0:
                print("Price cannot be negative.")
            else:
                break

        except ValueError:
            print("Please enter a valid price.")

    while True:
        try:
            stock = int(input("Stock Quantity: "))

            if stock < 0:
                print("Stock cannot be negative.")
            else:
                break

        except ValueError:
            print("Please enter a whole number.")

    product = Product(product_id, product_name, price, stock)

    inventory.add_product(product)

    print(f"{product_name} has been added successfully!")


# Update product stock
def update_stock():
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ").strip()

    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
        return

    while True:
        try:
            new_stock = int(input("Enter new stock quantity: "))

            if new_stock < 0:
                print("Stock cannot be negative.")
            else:
                break

        except ValueError:
            print("Please enter a valid whole number.")

    product.update_stock(new_stock)

    print("Stock updated successfully!")


# Search for a product
def search_product():
    print("\nSearch Product")

    product_id = input("Enter Product ID: ").strip()

    product = inventory.search_product(product_id)

    if product is not None:
        print("\nProduct found!")
        product.display_information()
    else:
        print("Product not found.")


# Get all product IDs
def get_all_product_ids():
    return [
        product.get_product_id()
        for product in inventory.get_all_products()
    ]


# Main program
def main():
    load_inventory()

    while True:
        display_menu()

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            add_product()

        elif choice == "3":
            update_stock()

        elif choice == "4":
            search_product()

        elif choice == "5":
            save_inventory()

        elif choice == "6":
            print("Exiting Inventory Management System.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()