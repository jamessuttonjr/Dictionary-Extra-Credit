class RetailItem:

    def __init__(self, description, inventory_units, price):
        self.__description = description
        self.__inventory_units = inventory_units
        self.__price = price

    def get_description(self):
        return self.__description

    def get_inventory_units(self):
        return self.__inventory_units

    def get_price(self):
        return self.__price

