from funtee.models.money import Money
from .product import Product

class CartItem:
    def __init__(self, product, size, quantity):
        self.product = product
        if size not in product.sizes:
            raise ValueError("Invalid size")
        else:
            self.size = size
        if quantity > 0:
            self._quantity = int(quantity)
        else:
            raise ValueError("Invalid quantity")
    def calculate_item_price(self):
        return Money(amount = (self.get_qty() * self.product.get_price()))
    def __str__(self):
        return f'nazwa produktu = {self.product.name}, rozmiar = {self.size}, ilość = {self.get_qty()}, cena całkowita = {self.calculate_item_price()}'
    def __repr__(self):
        return f"<CartItem product.sku = '{self.product.sku}'size = '{self.size}', quantity = {self.get_qty()}>"

    def get_qty(self):
        return self._quantity
    def set_qty(self, qty):
        if qty > 0:
            self._quantity = qty
        else:
            raise ValueError("Invalid quantity")
    def add_qty(self, qty):
        if qty > 0:
            self._quantity += qty
        else:
            raise ValueError("Invalid quantity")