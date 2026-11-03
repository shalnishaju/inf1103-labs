from product import Product


class Inventory:

    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id().lower() == product_id.lower():
                return product

        return None

    def display_all(self):
        print("\nCurrent Inventory")

        if not self.__products:
            print("Inventory is empty.")
            return

        for product in self.__products:
            product.display_information()
    def get_all_products(self):
        return self.__products
