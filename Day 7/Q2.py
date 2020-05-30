'''
 2. Write a Python class named Circle constructed by a radius and two
 methods which will compute the area and the perimeter of a circle.
'''

class circle:
    def __init__(s,r):
        s.r=r
    def area(s):
        print('Area of Circle',3.142*s.r*s.r)
    def perimeter(s):
        print('Perimeter of Circle',2*3.142*s.r)

c=circle(12)
c.area()
c.perimeter()
