with open("practice.txt","r+") as f:
    f.write("Hi everyone \nwe are learning file I/O \nusing Java \nI like learning programming in Java")

def rep(path="practice.txt"):
    with open("practice.txt","r+") as f:
        text=f.read()
        new= text.replace("Java","Python")
        f.seek(0)   #this will start the pointer from starting instead of at end
        f.write(new)
rep()

def c(path="practice.txt"):
    with open("practice.txt","r+") as f:
        l_count=f.read()
        word=l_count.find("learning")
        # print(word)
        if(word >=1):         #extra from me
            print("learning exist at idx",word)
        else:
            print("doesn't exist")

c()