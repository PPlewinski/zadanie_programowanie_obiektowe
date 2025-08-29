

class Product:
    TAX_RATE = 0.23

    @classmethod
    def from_dict(cls, data):
        return cls(sku=data['sku'], name=data['name'], base_price=data['base_price'], sizes=data['sizes'])

    @staticmethod
    def validate_sku(sku):
        if len(sku) < 5:
            return False
        else:
            return True

    def __init__(self, sku, name, base_price, sizes):
        if Product.validate_sku(sku):
            self.sku = str(sku)
        else:
            raise ValueError("Invalid SKU")
        self.name = str(name)
        self._base_price = float(base_price)
        self.sizes = list(sizes)

    def __str__(self):
        return f'SKU = {self.sku}, Nazwa = {self.name}, Cena = {self.get_price()}, Rozmiary = {self.sizes}'
    def __repr__(self):
        return f"<Product sku = '{self.sku}', name = '{self.name}', base_price = {self.get_price()}, sizes = '{self.sizes}'>"

    def __eq__(self, other):
        return self.sku == other.sku

    def get_price(self):
        return self._base_price
    def set_price(self, price):
        if price >= 0:
            self._base_price = price
        else:
            raise ValueError("Invalid price")