class Account :
    def __init__(self):
        self.__balance = 0.0
    def deposit(self, amount):
        if amount> 0:
            self.__balance += amount
        else:
            print("Invalid amount")
    def withdraw(self, amount):
        if amount <= self.__balance :
            amount -= self.__balance
            return amount
        else:
            print("Insufficient funds")
            return 0
        