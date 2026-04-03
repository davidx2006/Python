list1= [1,2,3,2,1]
list2= [1,"abc","abc",2]

cp_l1=list1.copy()
cp_l1.reverse()

cp_l2=list2.copy()
cp_l2.reverse()

if(cp_l1 == list1):
    print("list 1 is palindrome")
else:
    print("list 1 is not palindrome")

if(cp_l2 == list2):
    print("list 2 is palindrome")
else:
    print("list 2 is not palindrome")