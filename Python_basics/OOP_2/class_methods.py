class Person:
    name="anonymous"

    # def changename(self,name):
    #     self.name=name

    @classmethod
    def changename(cls,name):
        cls.name=name




p1= Person()
p1.changename("David")
print(Person.name)
print(p1.name)