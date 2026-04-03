f=open("demo.txt","w")   #overwrite the entire file

f.write("this is not a test subject")

f.close

f=open("sample.txt","w")    #creates a new file if not exist

f.write("this is sample file")

f.close