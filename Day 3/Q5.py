n=int(input("Enter no.:"))
l=[]
p=0
no=n
while True:
    if n==0:
        break
    t=n%10
    l.append(t)
    p+=1
    n=n//10
    
nn=0
for i in l:
    nn+=(i**p)
    
if nn==no:
    print(no,"is narcissistic number")
else:
    print(no,"is narcissistic number")
