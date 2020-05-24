a=[]
print("Enter 3X3 matrix:")
for i in range(0,3):
    l=[]
    for j in range(0,3):
        l.append(int(input()))
    a.append(l)

sum=0
for i in a:
    for j in i:
        sum+=j
print('Sum of matrix:',sum)
