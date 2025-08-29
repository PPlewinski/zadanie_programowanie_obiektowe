from funtee.models.cart_item import CartItem
from funtee.models.money import Money

class Order:
    def __init__(self, identification, created_at, status, total_paid, items=None,):
        self.identification = identification
        if items is None:
            items = []
        self.items = items
        self.created_at = created_at
        self._status = status
        self._total_paid = total_paid

    def __lt__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.get_total_paid() < other.get_total_paid()
    def __gt__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.get_total_paid()> other.get_total_paid()

    def get_status(self):
       return self._status
    def mark_paid(self):
        self._status = 'paid'
    def cancel(self):
        if self._status == 'paid':
            raise ValueError("Can't cancel order")
        else:
            self._status = 'canceled'
    def get_total_paid(self):
        return self._total_paid