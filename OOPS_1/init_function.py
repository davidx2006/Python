class Student:
    clg_name="Amity UNI"
    name="anonymouse"   #class attr
    def __init__(self, name, marks):
        self.name= name     #obj attr > class attr
        self.marks = marks
        print("Adding new student...")


s1 =Student("david", 88)
print(s1.name, s1.marks)

s2=Student("kalu", 22)
print(s2.name, s2.marks)

print(s2.clg_name)