from customer import Customer
from coffee import Coffee
from order import Order

# Sample Data Creation
customer1 = Customer("Alice")
customer2 = Customer("Bob")
coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

# Create Orders
order1 = Order(customer1, coffee1, 5.0)
order2 = Order(customer1, coffee2, 3.5)
order3 = Order(customer2, coffee1, 4.0)

# Test Relationships
print(f"{customer1.name}'s Orders:", [o.price for o in customer1.orders()])  
print(f"{coffee1.name}'s Customers:", [c.name for c in coffee1.customers()]) 

# Test Aggregates
print(f"{coffee1.name} Orders:", coffee1.num_orders())       
print(f"{coffee1.name} Avg Price:", coffee1.average_price()) 

# Test Immutability
try:
  coffee1.name = "Mocha"  # Should throw AttributeError
except AttributeError as e:
  print("Immutability Test Passed:", e)