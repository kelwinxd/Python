class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_data(self):
        self.name = input("type the name: ")
        self.price = int(input("type the price: "))

class Calculator(Product):
    result = 0
    def __init__(self, amount):
        self.amount = amount
    def howmuch(self):
        result = self.price * self.amount
        print(result)

       
calculate = Calculator(8)
calculate.get_data()
calculate.howmuch()