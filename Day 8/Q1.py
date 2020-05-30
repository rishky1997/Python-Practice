#1.Write a program to implement Constructor with Variable Number of Arguments.

class vnum:
    def __init__(s,*a):
        print(sum(a))

vnum(11,1,3)
vnum(22,2)
vnum(4,5,6,7,8)
