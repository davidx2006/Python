#example
class Complex:

    def __init__(self, real,img):
        self.real=real
        self.img=img

    def showno(self):
        print(self.real,"i +",self.img,"j")
    
    def __sub__(self,num2):
        newreal=self.real- num2.real
        newimg=self.img - num2.img
        return Complex(newreal,newimg)

com1=Complex(1,2)
com1.showno()

com2=Complex(4,8)
com2.showno()

com3=com1 -com2
com3.showno()