class Complex:

    def __init__(self, real,img):
        self.real=real
        self.img=img

    def showno(self):
        print(self.real,"i +",self.img,"j")

com1=Complex(1,2)
com1.showno()
com2=Complex(4,8)
com2.showno()