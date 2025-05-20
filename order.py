from customer import Customer
from coffee import Coffee

class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance.")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance.")
        self._customer = customer
        self._coffee = coffee
        self.price = price

        self._customer._orders.append(self)
        self._coffee._orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if hasattr(self, '_price'):
            raise AttributeError("Price cannot be changed after initialization.")
        if not isinstance(value, float):
            raise TypeError("Price must be a float.")
        if not (1.0 <= value <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")
        self._price = value