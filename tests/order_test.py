import unittest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder(unittest.TestCase):
    def test_price_validation(self):
        customer = Customer("Hank")
        coffee = Coffee("Cold Brew")
        with self.assertRaises(ValueError):
            Order(customer, coffee, 0.5)  
        with self.assertRaises(TypeError):
            Order(customer, coffee, "five")  

    def test_relationships(self):
        customer = Customer("Ivy")
        coffee = Coffee("Iced Coffee")
        order = Order(customer, coffee, 4.5)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.coffee, coffee)