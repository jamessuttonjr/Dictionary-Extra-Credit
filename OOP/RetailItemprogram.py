import RetailItemclass as r

def main():
    item1 = r.RetailItem("Jacket", 12, 59.95)
    item2 = r.RetailItem("Designer Jeans", 40, 34.95)
    item3 = r.RetailItem("Shirt", 20, 24.95)

    print(item1.get_description(), item1.get_inventory_units(), item1.get_price())
    print(item2.get_description(), item2.get_inventory_units(), item2.get_price())
    print(item3.get_description(), item3.get_inventory_units(), item3.get_price())

main()