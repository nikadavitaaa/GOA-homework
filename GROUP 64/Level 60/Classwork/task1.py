class Account:
    object_count = 0  

    def __init__(self, username, balance):
        self._balance = balance  
        self.__username = username  

        Account.object_count += 1  

    def _show_balance(self):
        return "Balance: " + str(self._balance)

    def __show_username(self):
        return "Username: " + self.__username

    def get_username(self):
        return self.__show_username()

    @classmethod
    def get_object_count(cls):
        return cls.object_count

acc1 = Account("Nika", 500)
acc2 = Account("Gio", 300)

print(acc1.get_username())
print(acc1._show_balance())
print(Account.get_object_count())
