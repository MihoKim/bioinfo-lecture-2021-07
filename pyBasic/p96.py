class Account():
    def __init__(self, balance, password):
        self.__password = password
        self.__balance = balance

    def deposit(self, out_balance, out_passwd):
        if self.__password != out_passwd:
            print("Password error!")
        elif self.__password == out_passwd:
            self.__balance += out_balance
            print(
                "Deposit is completed successfully. Your balance is {}".format(
                    self.__balance
                )
            )
        else:
            print("Please try again")

    def withdraw(self, out_balance, out_passwd):
        if self.__password != out_passwd:
            print("Password error!")
        elif self.__password == out_passwd:
            if out_balance > self.__balance:
                return
            else:
                self.__balance -= out_balance
                print(
                    "Withdraw is completed successfully. Your balance is {}".format(
                        self.__balance
                    )
                )
        else:
            print("Please try again")

    def transfer(self, other, out_balance, out_passwd):
        if self.__password != out_passwd:
            print("Password error!")
        elif self.__password == out_passwd:
            if out_balance > self.__balance:
                print("Not Enough Money")
                return
            else:
                self.__balance -= out_balance
                other.__balance += out_balance
                print(
                    "Transfer is completed successfully. Your balance is {}".format(
                        self.__balance
                    )
                )
                print(
                    f"Withdraw account's current balance is {self.__balance}"
                )
                print(
                    f"Deposit account's current balance is {other.__balance}"
                )
        else:
            print("Please try again")

    def showBalance(self, out_passwd):
        if self.__password != out_passwd:
            print("Password error!")
        elif self.__password == out_passwd:
            print(f"Your balance is {self.__balance}")

A = Account(0, 0000)
B = Account(10000, 1234)

A.deposit(10000, 0000)
A.deposit(5000, 1234)
A.withdraw(5000, 0000)

A.transfer(B, 3200, 0000)
A.transfer(B, 2500, 1234)

A.showBalance(0000)
B.showBalance(1234)


