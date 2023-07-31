class Account:

    def __init__(self,tittle,Balance):
        self.tittle=tittle
        self.Balance=Balance
class SavingsAccount(Account):

    def __init__(self,title, balance,interestRate):
        super().__init__(title, balance)
        self.interstRate=interestRate
         
savings_account = SavingsAccount("Ashish", 5000, 5)
print(savings_account.tittle)
print(savings_account.Balance)
print(savings_account.interstRate)
        
        