#4.Write a program to implement operator overloading in python.

class A:
    def __init__(s,a):
        s.a=a
    def __add__(s,o):
        return s.a+o.a
    def __sub__(s,o):
        return s.a-o.a
    def __mul__(s,o):
        return s.a*o.a
    def __truediv__(s,o):
        return s.a/o.a
    
a=A(2)
b=A(3)

print(a+b)
print(a-b)
print(a*b)
print(a/b)
