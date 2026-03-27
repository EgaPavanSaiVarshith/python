class Product:
    def __init__(self, name):
        self.name = name

    def display_product_details(self): 
        print("Superclass Method")

class ElectronicItem(Product):
    def display_product_details(self): # same method name as superclass
        print("Subclass Method")
 
e = ElectronicItem("Laptop")
e.display_product_details()
