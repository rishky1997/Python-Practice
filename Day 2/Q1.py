no=int(input("Enter a number:"))
sum=0
for i in range(1,no):
    sum=sum+i
    print(str(i),'+ ',end='')
print(str(no),end=' = ')
print(str(sum+no))
