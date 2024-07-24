from policyholder import Policyholder
from product import Product
from payment import Payment

# Create products
product1 = Product(product_id=1, name="Health Insurance", price=100)
product2 = Product(product_id=2, name="Life Insurance", price=200)

# Create policyholders
policyholder1 = Policyholder(policyholder_id=1, name="Alice")
policyholder2 = Policyholder(policyholder_id=2, name="Bob")

# Register policyholders for products
policyholder1.register(product1)
policyholder2.register(product2)

# Process payments
payment1 = Payment(policyholder=policyholder1, product=product1)
payment2 = Payment(policyholder=policyholder2, product=product2)

payment1.process_payment()
payment2.process_payment()

# Display policyholder details
policyholder1.display_details()
policyholder2.display_details()

# Simulate sending reminders and applying penalties
payment1.send_reminder()
payment2.send_reminder()

payment1.apply_penalty()
payment2.apply_penalty()

