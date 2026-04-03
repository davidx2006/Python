nums=(1,4,9,16,25,36,49,64,81,100,9)
x= 9
idx=0
for num in nums:
    if num == x:
        print("Found at index",idx)
    # else:
    #     print("Finding...")
    idx+=1
