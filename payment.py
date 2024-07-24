class Payment:
    def __init__(self, policyholder, product):
        self.policyholder = policyholder
        self.product = product
        self.paid = False

    def process_payment(self):
        self.paid = True

    def send_reminder(self):
        if not self.paid:
            print(f"Reminder: Payment due for {self.product.name}")

    def apply_penalty(self):
        if not self.paid:
            print(f"Penalty applied for {self.product.name}")

