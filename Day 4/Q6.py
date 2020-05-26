n=int(input("Enter no.:"))
def fdigit(no):
    while no!=0:
        f=no%10
        no=no//10
    return f

def ldigit(no):
    while no!=0:
        l=no%10
        return l

print("Sum of 1st digit and last digit:",fdigit(n)+ldigit(n))
