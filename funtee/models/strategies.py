

class Strategies:

    @staticmethod
    def default_strategy(total_price):
        return total_price

    @staticmethod
    def ten_per_strategy(total_price):
        return total_price * 0.9

    @staticmethod
    def minus_twenty_strategy(total_price):
        if total_price > 100:
            return total_price - 20
        return total_price
