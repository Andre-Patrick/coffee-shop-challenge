import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Customer("")  
        with self.assertRaises(TypeError):
            Customer(123)  

    def test_relationships(self):
        c = Customer("Charlie")
        coffee = Coffee("Cappuccino")
        order = Order(c, coffee, 6.0)
        self.assertIn(order, c.orders())
        self.assertIn(coffee, c.coffees())

    def test_create_order(self):
        c = Customer("Dave")
        coffee = Coffee("Americano")
        order = c.create_order(coffee, 4.5)
        self.assertIsInstance(order, Order)