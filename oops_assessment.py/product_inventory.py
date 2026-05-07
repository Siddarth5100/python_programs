class Product:
    # total_products_created = 0

    def __init__(self, name, price, quantity):
        self.name = name

        if price <= 0:
            print("Invalid price detected, setting default")
            self.__price = 1
        else:
            self.__price = price
        
        if quantity < 0:
            print("Invalid quantity detected, setting default")
            self.quantity = 1
        else:
            self.quantity = quantity
    
    def get_price(self):
        return self.__price
    
    def set_price(self, new_price):
        if new_price < self.__price:
            return "New price must be higher than current price"
        else:
            self.__price += new_price
            return "Price updated successfuly"
    
    def qty_avail(self):
        return f"Quantity avail: {self.quantity}"

    def total_value(self):
        total = self.__price * self.quantity
        return f"Product: {self.name}, Total Value: {total}"
    
    def sell(self, units):
        if units < self.quantity:
            self.quantity -= units
            return f"Sold: {units} units, Remaining stock: {self.quantity}"
        else:
            return f"Not enough stock"


pro = Product("Pen", 15, 10)

print(pro.total_value())
print(pro.qty_avail())
print(pro.sell(9))
print(pro.qty_avail())
# print(pro.price) '''this will throw error due to private'''
print(pro.get_price())
print(pro.set_price(15))
print(pro.get_price())

# pending => q4