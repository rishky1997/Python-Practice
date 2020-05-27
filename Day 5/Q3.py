#3.Write a Python program for Binary search.

a=[77,99,44,46,85,21,30,66,3,2,1]
a=sorted(a)

no=int(input("Enter no. to be search:"))
l=0
u=len(a)-1
flag=0

while l<=u:
    m=(l+u)//2
    if no>a[m]:
        l=m+1
    elif no<a[m]:
        u=m-1
    else:
        flag=1
        break
    
if flag==1:
    print("%d is present"%no)
else:
    print("%d is not present"%no)
