class Account:

    def __init__(self, bal, acno):
        self.balance= bal
        self.account_no=acno

    #Debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs", amount,"was debited from account no.",self.account_no,"\nTotal Balance Rs",self.balance)
        
    #Credit method
    def credit(self,cred):
        self.balance += cred
        print("Rs", cred,"was credited in account no.",self.account_no,"\nTotal Balance Rs",self.balance)


acc1=Account(23000, 2124992321)
# print(acc1.balance)
# print(acc1.account_no)
acc1.debit(2000)
acc1.credit(5000)