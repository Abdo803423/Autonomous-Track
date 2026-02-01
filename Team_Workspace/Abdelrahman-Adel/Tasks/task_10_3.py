from task_10_1 import PaymentMethod
class Cash(PaymentMethod) :
    def pay(self, amount) :
        print(f"Accepting Cash: {amount}")