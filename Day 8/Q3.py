#3.Write a program to implement multiple inheritance.

class A:
    def __init__(s):
        print('This is class X')
    def education(s):
        print("A's Education")
class B:
    def __init__(s):
        print('This is class X')
    def education(s):
        print("B's Education")
    def music(s):
        print("B's music")
class C:
    def __init__(s):
        print('This is class X')
    def education(s):
        print("c's Education")
    def music(s):
        print("'C's music")
    def sport(s):
        print("C's sport")
    
class X(A,B,C):
    def __init__(s):
        print('This is class X')

x=X()
x.education()
x.music()
x.sport()
