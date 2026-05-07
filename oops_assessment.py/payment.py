class Payment:
    def pay(self, amount):
        return amount

class UPI(Payment):
    pass

class Cash(Payment):
    pass


pay = Payment()
pay.pay(1000)

