
class Product:
    amount = 400
    result = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save_money(self, discount):
        
        result = self.price * discount / 100

        print(f'you will save {result}$')

p1 = Product('Shower Plug', 2500)
print(f'{p1.name} \n {p1.price}')
p1.save_money(10)