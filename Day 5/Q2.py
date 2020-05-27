#2.Write a Python program for sequential search (Linear search).

a=[77,99,44,46,85,21,30,66,3,2,1]

no=int(input("Enter no. to be search:"))
l=len(a)
for i in range(l):
    if a[i]==no:
        print(no,"is found")
        break
        
if i==l-1:
    print(no,"is not found")
