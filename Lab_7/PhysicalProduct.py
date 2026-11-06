from Product import Product
from CanBeShipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")
        print("-" * 48)

    def get_fulfilment_info(self):
        return "This product will be physically shipped to the customer."

    def calculate_shipping_cost(self):
        return self.__weight * 2
