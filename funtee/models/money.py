

class Money:
    def __init__(self, amount, currency = "PLN"):
        self.amount = float(amount)
        self.currency = currency

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Currencies do not match")
        return Money(self.amount + other.amount, self.currency)
    def __sub__(self, other):
        if self.currency != other.currency:
            raise ValueError("Currencies do not match")
        return Money(self.amount - other.amount, self.currency)
    def __mul__(self, other):
        if self.currency != other.currency:
            raise ValueError("Currencies do not match")
        return Money(self.amount * other, self.currency)
    def __truediv__(self, other):
        if self.currency != other.currency:
            raise ValueError("Currencies do not match")
        return Money(self.amount / other, self.currency)
    def __str__(self):
        return f"Money({self.amount}, {self.currency})"

    def __eq__(self, other):
        if self.currency != other.currency:
            raise ValueError("Currencies do not match")
        return self.amount == other.amount and self.currency == other.currency
    def __gt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Currencies do not match")
        return self.amount > other.amount and self.currency == other.currency
    def __lt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Currencies do not match")
        return self.amount < other.amount and self.currency == other.currency

    def __float__(self):
        return float(self.amount)

    def __bool__(self):
        if self.amount == 0:
            return False
        return True