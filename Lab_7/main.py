
import json
import os

from Product import Product
from Inventory import Inventory
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct


# Create an Inventory object
inventory = Inventory()


# Load inventory from JSON file
def load_inventory():
    if not os.path.exists("inventory.json"):
        # Create initial physical products if no JSON file exists
        product1 = PhysicalProduct("P001", "Laptop", 1200.00, 15, 2.5)
        product2 = PhysicalProduct("P002", "Mouse", 25.50, 40, 0.2)
        product3 = PhysicalProduct("P003", "Keyboard", 45.00, 25, 0.8)

        inventory.add_product(product1)
        inventory.add_product(product2)
        inventory.add_product(product3)

        return

    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)

        for item in data:
            product_type = item.get("type", "physical").lower()

            if product_type == "physical":
                product = PhysicalProduct(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item.get("weight", 0.0)
                )

            elif product_type == "digital":
                product = DigitalProduct(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["download_size"]
                )

            else:
                print(f"Unknown product type: {product_type}")
                continue

            inventory.add_product(product)

        print("Inventory loaded successfully!")

    except (json.JSONDecodeError, KeyError, TypeError, ValueError):
        print("Error loading inventory. Starting with an empty inventory.")


# Save inventory to JSON file
def save_inventory():
    products = []

    for product in inventory.get_all_products():

        if isinstance(product, PhysicalProduct):
            products.append({
                "type": "physical",
                "id": product.get_product_id(),
                "name": product.get_name(),
                "price": product.get_price(),
                "stock": product.get_stock(),
                "weight": product.get_weight()
            })

        elif isinstance(product, DigitalProduct):
            products.append({
                "type": "digital",
                "id": product.get_product_id(),
                "name": product.get_name(),
                "price": product.get_price(),
                "stock": product.get_stock(),
                "download_size": product.get_download_size()
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

    # Choose product type
    print("\nSelect Product Type")
    print("1. Physical Product")
    print("2. Digital Product")

    product_type = input("Enter your choice (1-2): ").strip()

    if product_type == "1":

        while True:
            try:
                weight = float(input("Weight (kg): "))

                if weight < 0:
                    print("Weight cannot be negative.")
                else:
                    break

            except ValueError:
                print("Please enter a valid weight.")

        product = PhysicalProduct(
            product_id, product_name, price, stock, weight
        )

    elif product_type == "2":

        while True:
            try:
                download_size = float(input("Download Size (MB): "))

                if download_size < 0:
                    print("Download size cannot be negative.")
                else:
                    break

            except ValueError:
                print("Please enter a valid download size.")

        product = DigitalProduct(
            product_id, product_name, price, stock, download_size
        )

    else:
        print("Invalid product type.")
        return

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
        print(product.get_fulfilment_info())

        if isinstance(product, PhysicalProduct):
            print(
                f"Shipping Cost: "
                f"${product.calculate_shipping_cost():.2f}"
            )

    else:
        print("Product not found.")


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
