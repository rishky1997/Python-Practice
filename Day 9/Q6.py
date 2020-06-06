#6.Write a python program to generate Fibonacci Numbers upto 100 using generator.


def fibo():
    a=0
    b=1
    while True:
        if a>100:
            break
        yield a
        a,b=b,a+b

for i in fibo():
    print(i)
