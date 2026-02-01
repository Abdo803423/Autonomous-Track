from task_10_1 import PaymentMethod
class CreditCard(PaymentMethod) :
    def pay(self, amount) :
        print(f"Processing Credit Card: {amount}")