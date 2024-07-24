class Policyholder:
    def __init__(self, policyholder_id, name):
        self.policyholder_id = policyholder_id
        self.name = name
        self.active = True
        self.products = []

    def register(self, product):
        if self.active:
            self.products.append(product)
        else:
            print("Policyholder is suspended and cannot register for products.")

    def suspend(self):
        self.active = False

    def reactivate(self):
        self.active = True

    def display_details(self):
        print(f"ID: {self.policyholder_id}, Name: {self.name}, Active: {self.active}")
        for product in self.products:
            print(f" - Product: {product.name}")

