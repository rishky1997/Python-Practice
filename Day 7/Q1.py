'''
1.Write python program to perform bank operations using class and objects.
       Conditions:
a.Bank name should be static.
b.Using menu driven program.
1 .Deposit
2. Withdraw
3. Exit
'''
class bank:
    name='SBI'
    def __init__(s):
        s.bal=0
    def deposit(s,a):
        s.bal+=a
        print("Balance:",s.bal)
    def withdraw(s,a):
        s.bal-=a
        print("Balance:",s.bal)
b=bank()    
while True:
    print("Welcome to",b.name,'Bank')
    print("Your Balance is:",b.bal)
    n=int(input("Enter your options:\n1 .Deposit\n2. Withdraw\n3. Exit\n"))
    if n==1:
        amt=float(input("Enter your amount to deposit:"))
        b.deposit(amt)
    elif n==2:
        amt=float(input("Enter your amount to withdraw:"))
        b.withdraw(amt)
    elif n==3:
        break
    else:
        print("Check your option")
