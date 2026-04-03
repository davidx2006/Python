dict={}
sub3= float(input("Enter your maths marks: "))
sub1= float(input("Enter your physics marks: "))
sub2= float(input("Enter your chemistry marks: "))

dict.update({"maths": sub1})
dict.update({"chemistry":sub2})
dict.update({"physics":sub3})

print(dict)