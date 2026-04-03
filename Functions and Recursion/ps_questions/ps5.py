def cal(n):
    if(n == 0):
        return 0
    return cal(n-1)+n

sum=cal(5)
print(sum)