with open("demo.txt","w") as f:
    f.write("david.ai")


with open("demo.txt", "r") as f:
    data= f.read()
    print(data)