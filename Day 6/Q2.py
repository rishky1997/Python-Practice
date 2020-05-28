#2.Write program to implement Selection sort.

no=[5,6,1,2,3]
l=len(no)
for i in range(l-1):
    for j in range(i+1,l):
        if no[i]>no[j]:
            no[i],no[j]=no[j],no[i]

print(no)
