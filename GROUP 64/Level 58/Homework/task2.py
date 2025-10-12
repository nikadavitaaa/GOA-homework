class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} ₾ დაემატა ბალანსს.")
        else:
            print("თანხა უნდა იყოს დადებითი.")

    def show_balance(self):
        print(f"ბალანსი: {self.balance} ₾")
