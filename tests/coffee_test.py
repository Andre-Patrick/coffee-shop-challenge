import unittest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee(unittest.TestCase):
    def test_name_immutability(self):
        coffee = Coffee("Mocha")
        with self.assertRaises(AttributeError):
            coffee.name = "Frappe"

    def test_average_price(self):
        coffee = Coffee("Flat White")
        Order(Customer("Eve"), coffee, 5.0)
        Order(Customer("Frank"), coffee, 7.0)
        self.assertEqual(coffee.average_price(), 6.0)

    def test_customers_uniqueness(self):
        coffee = Coffee("Macchiato")
        customer = Customer("Grace")
        Order(customer, coffee, 3.0)
        Order(customer, coffee, 4.0)
        self.assertEqual(len(coffee.customers()), 1)