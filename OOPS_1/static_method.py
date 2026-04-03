class Student:
    def __init__(self,name, marks,):
        self.name= name
        self.marks=marks

    @staticmethod
    def hello():
        print("Hello")


    def avg(self):
        sum=0
        for val in self.marks:
            sum += val
        print("The avg of",self.name,"is :",sum/3)
                
s1=Student("Thanos",[99,92,95])
s1.hello()
s1.avg()
