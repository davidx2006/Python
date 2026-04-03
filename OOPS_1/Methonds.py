class Student:
    def __init__(self, name, marks):
        self.name= name     #obj attr > class attr
        self.marks=marks

    def welcome(self):
        print("Welcone student", s1.name)

    def get_marks(self):
        return self.marks

s1=Student("david",99)
s1.welcome()
print(s1.get_marks())



