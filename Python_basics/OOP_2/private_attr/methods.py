class Account:
    def __init__(self, acc_no, acc_pass):
        self.accno=acc_no
        self.__accpass=acc_pass    #private

    def reset_pass(self):
        print(self.__accpass)

acc1= Account(12345,3332)
print(acc1.accno)
# print(acc1.accpass)
acc1.reset_pass()


#Next example

class Person:
    __name= "david"

    def __helo(self):
        print("Hello User!")
    
    def welcome(self):
        self.__helo()

nam1= Person()
print(nam1.welcome())
