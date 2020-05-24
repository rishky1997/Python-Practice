l=[1,2.2,'hello',4,5,'hi',10.00,20.20]
i=[]
s=[]
f=[]
for n in l:
    if type(n)==int:
        i.append(n)
    if type(n)==str:
        s.append(n)
    if type(n)==float:
        f.append(n)
print(i)
print(s)
print(f)
