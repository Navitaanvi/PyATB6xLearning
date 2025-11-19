class Bank:
    def __init__(self,account_number,balance):
        self.balance = balance
        self.__account_number = account_number


    def check_balance(self):
        print(self.balance)

    def deposit(self,amount):
        self.balance = self.balance + amount

    def show_me_account_number(self,auth):
        if auth == True:
            print(self.__account_number)
        else:
            print("Not Allowed")

icici = Bank(125676389,100000)
icici.check_balance()
icici.deposit(20000)
# icici.check_balcance()
icici.show_me_account_number(True)


