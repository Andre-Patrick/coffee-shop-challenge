from coffee import Coffee

class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters.")
        self._name = value

    def orders(self):
        return self._orders.copy()

    def coffees(self):
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance.")
        orders = coffee.orders()
        if not orders:
            return None
        customer_totals = {}
        for order in orders:
            customer = order.customer
            customer_totals[customer] = customer_totals.get(customer, 0.0) + order.price
        max_total = max(customer_totals.values())
        for customer, total in customer_totals.items():
            if total == max_total:
                return customer
        return None