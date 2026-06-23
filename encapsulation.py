class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def show__balance(self):
        print("Balance:", self.__balance)

acc = BankAccount(11000)
acc.deposit(2000)
acc.withdraw(3000)
acc.show__balance()