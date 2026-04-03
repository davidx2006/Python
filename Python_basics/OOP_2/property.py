class Student:
    def __init__(self,phy,chem,maths):
        self.physics=phy
        self.chem=chem
        self.maths=maths
    
    @property
    def percentage(self):
        return str((self.physics+self.chem+self.maths)/3)+ "%"


stu1=Student(90,80,70)
stu1.physics=85
print(stu1.percentage)