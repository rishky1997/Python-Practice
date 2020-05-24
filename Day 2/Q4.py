o=1
a=[]
for i in range(1,6):
    l=[]
    print(' '*(6-i),end='')
    for j in range(1,i+1):
        print(str(o),end=' ')
        l.append(o)
        o+=2
    print('')
    a.append(l)


def row_sum_odd_numbers(n):
    l=a[n-1]
    for i in range(0,len(l)-1):
        print(str(l[i]),'+ ',end='')
    print(str(l[i+1]),end=' = ')
    print(sum(l))
