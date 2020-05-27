#1.Write a Python program to sort a list of elements using the bubble sort Algorithm.


def bsort(no):
    l=len(no)
    for i in range(l-1):
        for j in range(l-1):
            if a[j]>a[j+1]:
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t


a=[77,99,2,3,1,44,2,46,85,21,30,66,3,2,1]
bsort(a)
print(a)
