name= ["david","milind","moki"]

def out(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    out(list,idx+1)
    
out(name)