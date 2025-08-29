from funtee.models.cart import Cart
from funtee.models.cart_item import CartItem
from funtee.models.product import Product
from funtee.models.order import Order
from funtee.models.money import Money
from funtee.models.strategies import Strategies

is_even = lambda x: x%2 == 0
def program_runner():
    product = Product(sku = "eqafaa", name = "koszulka zebra", base_price = 100, sizes = ["S", "M", "L"])
    product_1 = Product(sku = "23dda", name = "koszulka żyrafa", base_price = 100, sizes = ["S", "M", "L"])
    cart_item1 = CartItem(product, 'M', 1)
    cart_item2 = CartItem(product_1, 'L', 2)
    cart = Cart(name = "zamówienie", items=[cart_item1, cart_item2], pricing_strategy = Strategies.minus_twenty_strategy)
    print(cart)
    print(cart.total_base())
    cart.add_item(product, 'M', 1)
    print(cart.total_base())
    # cart.remove_item('23dda', 'L')
    # print(cart.total_base())
    # print(cart)
    # print()
    # print(product)
    # print()
    # print([product])
    # print()
    # print(cart_item1)
    # print()
    print(cart.__len__())
    # print()
    # print(cart.__bool__())
    # print()
    cart_2 = Cart("Siema")
    print(cart_2.__bool__())
    order_1 = Order(identification="1", items=cart.items, created_at="Teraz", status="In realisation", total_paid=cart.total_base())
    order_2 = Order(identification="2", items=[cart_item1], created_at="Teraz", status="In realisation", total_paid=cart_item1.calculate_item_price())
    print(order_1 > order_2)
    print(order_1 < order_2)
    print(cart.total_base())
    print(type(cart.total_base()))
    money_1 = Money(amount = 100, currency = "PLN")
    money_2 = Money(amount = 200, currency = "PLN")
    print(money_1 + money_2)
    print(money_1 - money_2)
    print(money_1 * 3)
    print(money_1 / 3)
    data = {
        'sku': "dawca32",
        'name': "koszulka biała",
        'base_price': 100,
        'sizes': ['S', 'M', 'L'],
    }
    product = Product.from_dict(data)
    print(product)
    print(cart)
    cart.items.sort(key = lambda item: item.calculate_item_price(), reverse = True)
    print(cart)
    print(is_even(4))
    print(is_even(5))
    product_data = {
        'sku': "dawca32",
        'name': "dsdsf",
        'base_price': 100,
        'sizes': ['S', 'M', 'L'],
    }
    product = Product(**product_data)
    print(product)
if __name__ == '__main__':
    program_runner()
