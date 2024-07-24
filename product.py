class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def update(self, name, price):
        self.name = name
        self.price = price

    def suspend(self):
        self.suspended = True

