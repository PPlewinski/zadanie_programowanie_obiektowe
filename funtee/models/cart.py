from .cart_item import CartItem
from funtee.models.money import Money
from funtee.models.strategies import Strategies

class Cart:

    def __init__(self, name, items = None, pricing_strategy = None):
        self.name = name
        if items is None:
            items = []
        if type(items) is not list:
            raise TypeError('items must be a list')
        self.items = items
        if pricing_strategy is None:
            pricing_strategy = Strategies.default_strategy
        self.pricing_strategy = pricing_strategy

    def total_base(self):
        total = 0
        for item in self.items:
            total += item.product.get_price() * item.get_qty()
        return Money(self.pricing_strategy(total))

    def add_item(self, product, size, quantity):
        for item in self.items:
            if item.product.sku == product.sku and item.size == size:
                item.add_qty(quantity)
                return
        self.items.append(CartItem(product, size, quantity))

    def remove_item(self, sku, size):
        for item in self.items:
            if item.product.sku == sku and item.size == size:
                self.items.remove(item)
                return True
        return False

    def __str__(self):
        name = f'nazwa = {self.name}'
        total =  f'cena całkowita = {self.total_base()}'
        lista = "Lista produktów:\n"
        for item in self.items:
            lista += f'{item.__str__()},\n'
        result = "\n".join([name, total, lista])
        return result

    def __len__(self):
        return sum(item.get_qty() for item in self.items)

    def __bool__(self):
        return bool(self.items)

    def __add__(self, other):
        return Cart(self.name, self.items + other.items)
    def __eq__(self, other):
        return self.items == other.items



