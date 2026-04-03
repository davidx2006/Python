class A:
    varA= "This is class A"

class B:
    varB= "This is class B"

class C(A, B):
    varC= "This is class C"

var= C()
print(var.varB)
print(var.varC)
print(var.varA)